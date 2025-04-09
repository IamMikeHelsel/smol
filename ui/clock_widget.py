"""
Clock Widget for PyWeatherClock.
Main UI component displaying time, date, and weather information.
"""

import customtkinter as ctk
from PIL import Image, ImageTk, ImageFont
import time
from datetime import datetime
import logging
import os
import threading

logger = logging.getLogger('PyWeatherClock.UI')

class ClockWidget(ctk.CTkFrame):
    """Main widget displaying time, date, and weather information"""
    
    def __init__(self, master, config, weather_api, **kwargs):
        super().__init__(master, **kwargs)
        
        self.logger = logger
        self.config = config
        self.weather_api = weather_api
        
        # Font configurations
        self.time_font_size = config.get('ui', {}).get('time_font_size', 48)
        self.date_font_size = config.get('ui', {}).get('date_font_size', 24)
        self.weather_font_size = config.get('ui', {}).get('weather_font_size', 18)
        
        # Format configurations
        self.time_format = config.get('time', {}).get('format', '%H:%M:%S')
        self.date_format = config.get('date', {}).get('format', '%A, %B %d')
        
        # Update intervals
        self.time_update_interval = config.get('time', {}).get('update_interval', 1000)
        self.weather_update_interval = config.get('weather', {}).get('update_interval', 900000)
        
        # Create UI components
        self._init_ui()
        
        # Start update loops
        self._update_time()
        self._update_weather()
    
    def _init_ui(self):
        """Initialize UI components"""
        # Configure the frame
        self.configure(corner_radius=10)
        
        # Create vertical layout frames
        self.time_frame = ctk.CTkFrame(self, corner_radius=0)
        self.time_frame.pack(fill="x", padx=10, pady=(10, 5))
        
        self.date_frame = ctk.CTkFrame(self, corner_radius=0)
        self.date_frame.pack(fill="x", padx=10, pady=5)
        
        self.weather_frame = ctk.CTkFrame(self, corner_radius=0)
        self.weather_frame.pack(fill="x", padx=10, pady=(5, 10))
        
        # Create labels for displaying information
        self.time_label = ctk.CTkLabel(
            self.time_frame, 
            text="00:00:00", 
            font=ctk.CTkFont(size=self.time_font_size)
        )
        self.time_label.pack(pady=5)
        
        self.date_label = ctk.CTkLabel(
            self.date_frame, 
            text="Loading date...", 
            font=ctk.CTkFont(size=self.date_font_size)
        )
        self.date_label.pack(pady=5)
        
        # Weather display (horizontal layout)
        self.weather_frame.columnconfigure(0, weight=1)
        self.weather_frame.columnconfigure(1, weight=1)
        self.weather_frame.columnconfigure(2, weight=1)
        
        self.weather_icon_label = ctk.CTkLabel(
            self.weather_frame, 
            text="🌡️", 
            font=ctk.CTkFont(size=self.weather_font_size + 10)
        )
        self.weather_icon_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.weather_temp_label = ctk.CTkLabel(
            self.weather_frame, 
            text="--°C", 
            font=ctk.CTkFont(size=self.weather_font_size)
        )
        self.weather_temp_label.grid(row=0, column=1, padx=5, pady=5)
        
        self.weather_desc_label = ctk.CTkLabel(
            self.weather_frame, 
            text="Loading weather...", 
            font=ctk.CTkFont(size=self.weather_font_size)
        )
        self.weather_desc_label.grid(row=0, column=2, padx=5, pady=5)
        
    def _update_time(self):
        """Update time and date display"""
        try:
            # Get current time and date
            now = datetime.now()
            time_str = now.strftime(self.time_format)
            date_str = now.strftime(self.date_format)
            
            # Update labels
            self.time_label.configure(text=time_str)
            self.date_label.configure(text=date_str)
            
        except Exception as e:
            self.logger.error(f"Error updating time: {e}")
        
        # Schedule next update
        self.after(self.time_update_interval, self._update_time)
    
    def _update_weather(self):
        """Update weather display"""
        try:
            # Try to get weather data
            weather_data = self.weather_api.get_weather()
            error = self.weather_api.get_error()
            
            if weather_data:
                # Update weather display with data
                self.weather_icon_label.configure(text=weather_data['icon_symbol'])
                self.weather_temp_label.configure(text=weather_data['temperature'])
                self.weather_desc_label.configure(text=weather_data['description'])
            elif error:
                # Display error message
                self.weather_icon_label.configure(text="❓")
                self.weather_temp_label.configure(text="--")
                self.weather_desc_label.configure(text=f"Error: {error}")
            else:
                # Still loading
                self.weather_icon_label.configure(text="🔄")
                self.weather_temp_label.configure(text="--")
                self.weather_desc_label.configure(text="Loading...")
                
            # Request fresh data
            self.weather_api.update_weather()
            
        except Exception as e:
            self.logger.error(f"Error updating weather display: {e}")
            self.weather_desc_label.configure(text="Display error")
        
        # Schedule next update
        self.after(self.weather_update_interval, self._update_weather)
    
    def set_custom_font(self, font_path):
        """
        Set custom font for the widget if the font file exists
        
        Args:
            font_path (str): Path to .ttf or .otf font file
        """
        if not font_path or not os.path.exists(font_path):
            self.logger.warning(f"Custom font file not found: {font_path}")
            return False
        
        try:
            # This requires more complex handling with CTk and is 
            # currently just a placeholder for future implementation
            # as CustomTkinter doesn't directly support custom TTF loading
            self.logger.info(f"Custom font set: {font_path}")
            return True
        except Exception as e:
            self.logger.error(f"Error setting custom font: {e}")
            return False
