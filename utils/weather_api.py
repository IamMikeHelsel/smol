"""
Weather API interface for PyWeatherClock.
Handles fetching and processing weather data from OpenWeatherMap.
"""

import requests
import logging
import threading
import time
from requests.exceptions import RequestException

logger = logging.getLogger('PyWeatherClock.Weather')

class WeatherAPI:
    """Interface for fetching weather data from OpenWeatherMap API"""
    
    def __init__(self, config):
        self.logger = logger
        self.config = config
        self.weather_data = None
        self.error = None
        self.api_key = config.get('weather', {}).get('api_key', '')
        self.location = config.get('weather', {}).get('location', 'London')
        self.units = config.get('weather', {}).get('units', 'metric')
        
        # Base URL for OpenWeatherMap API
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        
        # Weather icons mapping (OpenWeatherMap icon codes to descriptions)
        self.weather_icons = {
            "01d": "☀️",  # clear sky day
            "01n": "🌙",  # clear sky night
            "02d": "⛅",  # few clouds day
            "02n": "☁️",  # few clouds night
            "03d": "☁️",  # scattered clouds
            "03n": "☁️",  # scattered clouds
            "04d": "☁️",  # broken clouds
            "04n": "☁️",  # broken clouds
            "09d": "🌧️",  # shower rain
            "09n": "🌧️",  # shower rain
            "10d": "🌦️",  # rain day
            "10n": "🌧️",  # rain night
            "11d": "⛈️",  # thunderstorm
            "11n": "⛈️",  # thunderstorm
            "13d": "❄️",  # snow
            "13n": "❄️",  # snow
            "50d": "🌫️",  # mist
            "50n": "🌫️",  # mist
        }
        
        # Initial weather fetch
        self.update_weather()
    
    def update_weather(self):
        """Fetch updated weather data from API"""
        threading.Thread(target=self._fetch_weather_data, daemon=True).start()
    
    def _fetch_weather_data(self):
        """Fetch weather data from OpenWeatherMap API in a separate thread"""
        if not self.api_key:
            self.logger.warning("No API key configured. Weather data will not be available.")
            self.error = "No API key"
            return
        
        try:
            params = {
                'q': self.location,
                'appid': self.api_key,
                'units': self.units
            }
            
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            self.logger.debug(f"Weather data received: {data}")
            
            # Process data into a more usable format
            processed_data = self._process_weather_data(data)
            self.weather_data = processed_data
            self.error = None
            
            self.logger.info(f"Weather updated for {self.location}: {processed_data['description']}, {processed_data['temperature']}")
            
        except RequestException as e:
            self.logger.error(f"Error fetching weather data: {e}")
            self.error = "Connection error"
        except ValueError as e:
            self.logger.error(f"Error parsing weather data: {e}")
            self.error = "Data error"
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")
            self.error = "Unknown error"
    
    def _process_weather_data(self, data):
        """Process raw weather data into a usable format"""
        temp = data['main']['temp']
        temp_unit = "°C" if self.units == "metric" else "°F"
        
        weather_id = data['weather'][0]['id']
        weather_main = data['weather'][0]['main']
        weather_description = data['weather'][0]['description'].capitalize()
        weather_icon_code = data['weather'][0]['icon']
        
        # Get icon symbol from mapping or fallback
        icon_symbol = self.weather_icons.get(weather_icon_code, "🌡️")
        
        return {
            'temperature': f"{round(temp)}{temp_unit}",
            'temp_value': temp,
            'temp_unit': temp_unit,
            'description': weather_description,
            'main': weather_main,
            'icon_code': weather_icon_code,
            'icon_symbol': icon_symbol,
            'city': data['name'],
            'country': data['sys']['country'],
            'humidity': f"{data['main']['humidity']}%",
            'wind_speed': data['wind']['speed'],
            'timestamp': time.time()
        }
    
    def get_weather(self):
        """
        Get current weather data
        
        Returns:
            dict: Weather data or None if not available
        """
        return self.weather_data
    
    def get_error(self):
        """
        Get current error state
        
        Returns:
            str: Error message or None if no error
        """
        return self.error
    
    def set_location(self, location):
        """
        Set a new location and update weather
        
        Args:
            location (str): City name or ZIP code
        """
        self.location = location
        self.update_weather()
    
    def set_units(self, units):
        """
        Set temperature units and update weather
        
        Args:
            units (str): 'metric' for Celsius or 'imperial' for Fahrenheit
        """
        if units in ['metric', 'imperial']:
            self.units = units
            self.update_weather()
        else:
            self.logger.warning(f"Invalid units value: {units}. Must be 'metric' or 'imperial'.")
    
    def set_api_key(self, api_key):
        """
        Set new API key and update weather
        
        Args:
            api_key (str): OpenWeatherMap API key
        """
        self.api_key = api_key
        self.update_weather()
