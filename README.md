# PyWeatherClock

A lightweight, visually appealing desktop widget built in Python that displays time, date, and weather information.

## Features

- **Time Display**: Shows current time in configurable format
- **Date Display**: Shows current date in configurable format
- **Weather Information**: 
  - Current temperature (°C or °F)
  - Weather condition with icon
  - Location-based weather data
- **Customization**:
  - Dark/Light/System theme
  - Configurable update intervals
  - Adjustable transparency
  - Borderless window with drag support
  - Stay-on-top functionality

## Installation

1. Clone this repository:
```
git clone https://github.com/yourusername/pyweatherclock.git
cd pyweatherclock
```

2. Install required dependencies:
```
pip install -r requirements.txt
```

3. Set up OpenWeatherMap API key:
   - Create a free account at [OpenWeatherMap](https://openweathermap.org/)
   - Generate an API key
   - Update the configuration file (the app will prompt you on first run)

## Usage

Run the application:
```
python pyweatherclock.py
```

### Configuration

The application will create a configuration file on first run. You can modify the settings by:

1. Right-clicking on the widget and selecting "Settings" (future feature)
2. Manually editing the config file located at:
   - Windows: `%APPDATA%\PyWeatherClock\PyWeatherClock\config.json`
   - macOS: `~/Library/Application Support/PyWeatherClock/PyWeatherClock/config.json`
   - Linux: `~/.config/PyWeatherClock/PyWeatherClock/config.json`

### Available Settings

- **Weather**:
  - `api_key`: Your OpenWeatherMap API key
  - `location`: City name (e.g., "London")
  - `units`: "metric" (°C) or "imperial" (°F)
  - `update_interval`: Weather update frequency in milliseconds

- **UI**:
  - `theme`: "System", "Dark", or "Light"
  - `borderless`: true/false - Whether to show window borders
  - `stay_on_top`: true/false - Whether window stays on top of other windows
  - `transparency`: 0.0-1.0 - Window transparency level

- **Time/Date**:
  - `time.format`: Time format string (e.g., "%H:%M:%S")
  - `date.format`: Date format string (e.g., "%A, %B %d")

## Requirements

- Python 3.6+
- Dependencies listed in requirements.txt:
  - customtkinter
  - requests
  - pillow
  - appdirs

## License

See the [LICENSE](LICENSE) file for details.
