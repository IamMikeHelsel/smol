"""
Configuration manager for PyWeatherClock.
Handles loading, saving, and providing default settings.
"""

import os
import json
import logging
import appdirs
from pathlib import Path

logger = logging.getLogger('PyWeatherClock.Config')

class ConfigManager:
    """Manages configuration settings for PyWeatherClock application"""
    
    def __init__(self):
        self.logger = logger
        
        # Set up config directory and file paths
        self.app_name = "PyWeatherClock"
        self.app_author = "PyWeatherClock"
        self.config_dir = appdirs.user_config_dir(self.app_name, self.app_author)
        self.config_file = os.path.join(self.config_dir, "config.json")
        
        # Ensure the config directory exists
        try:
            os.makedirs(self.config_dir, exist_ok=True)
            self.logger.info(f"Using configuration directory: {self.config_dir}")
        except Exception as e:
            self.logger.error(f"Failed to create config directory {self.config_dir}: {e}")
            self.logger.warning("Will attempt to use current directory for configuration")
            self.config_dir = os.path.dirname(os.path.abspath(__file__))
            self.config_file = os.path.join(os.path.dirname(self.config_dir), "config.json")
        
        # Default configuration
        self.default_config = {
            "weather": {
                "api_key": "",  # OpenWeatherMap API key
                "location": "London",  # Default location
                "units": "metric",  # metric or imperial
                "update_interval": 900000  # 15 minutes in milliseconds
            },
            "time": {
                "format": "%H:%M:%S",  # 24-hour format with seconds
                "update_interval": 1000  # 1 second in milliseconds
            },
            "date": {
                "format": "%A, %B %d"  # e.g., "Tuesday, April 8"
            },
            "ui": {
                "theme": "Dark",  # System, Dark, or Light
                "color_theme": "blue",
                "font_path": "",  # Custom font path if specified
                "time_font_size": 48,
                "date_font_size": 24,
                "weather_font_size": 18,
                "width": 400,  # Made wider for better visibility
                "height": 300,  # Made taller for better visibility
                "transparency": 1.0,  # Set to fully opaque for first run
                "borderless": False,  # Disabled borderless mode for easier visibility
                "stay_on_top": True
            }
        }
    
    def load_config(self):
        """
        Load configuration from file or create default if not exists
        
        Returns:
            dict: Configuration dictionary
        """
        # If config file exists, load it
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                self.logger.info(f"Loaded configuration from {self.config_file}")
                
                # Merge with default config to ensure all keys exist
                self._merge_with_defaults(config)
                return config
            except json.JSONDecodeError as e:
                self.logger.error(f"Invalid JSON in config file: {e}")
                self.logger.info("Using default configuration")
                return self.default_config
            except Exception as e:
                self.logger.error(f"Error loading config file: {e}")
                self.logger.info("Using default configuration")
                return self.default_config
        else:
            # Create default config file
            self.logger.info(f"No config file found, creating default at {self.config_file}")
            try:
                self.save_config(self.default_config)
                return self.default_config
            except Exception as e:
                self.logger.error(f"Failed to create default config file: {e}")
                self.logger.warning("Using default configuration in memory only")
                return self.default_config
    
    def save_config(self, config):
        """
        Save configuration to file
        
        Args:
            config (dict): Configuration to save
        """
        try:
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=4)
            self.logger.info(f"Saved configuration to {self.config_file}")
            return True
        except Exception as e:
            self.logger.error(f"Error saving config file: {e}")
            return False
    
    def _merge_with_defaults(self, config):
        """
        Ensure all default keys exist in the config
        
        Args:
            config (dict): Configuration to update
        """
        # Recursively update config with any missing keys from default
        for key, value in self.default_config.items():
            if key not in config:
                config[key] = value
            elif isinstance(value, dict):
                if not isinstance(config[key], dict):
                    config[key] = value
                else:
                    for subkey, subvalue in value.items():
                        if subkey not in config[key]:
                            config[key][subkey] = subvalue
