
# PyWeatherClock - Desktop Widget

## 1. Overview

A lightweight, visually appealing desktop application built entirely in Python. It displays the current time, date, and weather information for a user-configured location. The primary goals are aesthetic appeal, minimal resource usage, and reliable performance.

## 2. Core Features

* **Time Display:** Shows the current local time (HH:MM:SS or HH:MM format, configurable).
* **Date Display:** Shows the current local date (e.g., "Tuesday, April 8" or "YYYY-MM-DD", configurable).
* **Weather Display:**
  * Current temperature (°C or °F, configurable).
  * Current weather condition description (e.g., "Clear", "Partly Cloudy").
  * Weather icon representing the current condition.
  * Configurable location (City name or ZIP code).
* **Customization:**
  * User-selectable font for time/date display.
  * User-configurable location.
  * User-selectable temperature units (Celsius/Fahrenheit).
  * User-configurable time/date formats.
* **Automatic Updates:**
  * Time/Date updates every second.
  * Weather information updates periodically (e.g., every 15-30 minutes).

## 3. Technical Stack

* **Language:** Python 3.x
* **UI Framework:**
  * **Recommended:** `CustomTkinter` - Provides modern-looking widgets and theming capabilities on top of Tkinter, simplifying the creation of an aesthetically pleasing UI.
  * **Alternative:** `Tkinter` (built-in) - Simpler, fewer dependencies, but requires more effort for custom styling.
* **HTTP Requests:** `requests` library - For fetching weather data from an API.
* **Weather Data API:**
  * **Recommended:** OpenWeatherMap (openweathermap.org) - Offers a free tier suitable for this application's needs (requires API key).
  * **Alternative:** WeatherAPI.com, or other similar services.
* **Configuration:**
  * `configparser` (built-in) or `json` (built-in) - For reading/writing user settings (location, API key, units, font preference) from/to a configuration file (e.g., `config.ini` or `config.json`).
* **Date/Time:** `datetime` module (built-in).
* **Packaging (Optional):** `PyInstaller` - To bundle the application and its dependencies into a standalone executable for easier distribution.

## 4. UI Design & Layout

* **Window:**
  * Small, borderless/minimal border window (user-configurable or fixed).
  * Should ideally stay on top (optional, configurable).
  * Background should be semi-transparent or match a theme (using CustomTkinter's capabilities).
* **Layout:**
  * Vertical stack layout is recommended for simplicity.
  * **Section 1 (Top):** Time display (large, prominent font).
  * **Section 2 (Middle):** Date display (smaller font than time).
  * **Section 3 (Bottom):** Weather information:
    * Horizontally arranged: Weather Icon | Temperature | Condition Description.
* **Fonts:**
  * Application must load and use a user-specified `.ttf` or `.otf` font file for the Time/Date display. The path to the font file will be stored in the configuration. Provide a default fallback font.
* **Weather Icons:**
  * Use a dedicated weather icon font (e.g., Weather Icons - [github.com/erikflowers/weather-icons]([invalid%20URL%20removed])) or map API condition codes to a set of bundled image files (e.g., PNGs). Icon font is generally more scalable.
* **Theming:** Leverage `CustomTkinter`'s built-in themes ("System", "Dark", "Light") or define a custom color scheme.

## 5. Data Handling

* **Time/Date:**
  * Use `datetime.datetime.now()` to get current time/date.
  * Use `strftime()` for formatting according to configuration.
  * Schedule updates using the UI framework's timer mechanism (e.g., `root.after()` in Tkinter/CustomTkinter) every 1000ms (1 second).
* **Weather:**
  * Fetch data from the chosen Weather API using the `requests` library.
  * Parse the JSON response to extract required fields (temperature, description, icon code).
  * Handle API key authentication.
  * Implement unit conversion (Kelvin from API to C/F).
  * Schedule updates using `root.after()` at a configurable interval (e.g., 900,000ms = 15 minutes).
  * **Crucial:** Perform API calls in a separate thread (`threading` module) or use an async approach (if using an async-compatible UI framework) to avoid blocking the UI thread and maintain responsiveness.
* **Configuration:**
  * On startup, load settings from `config.ini` or `config.json` located in a user-specific configuration directory (use `appdirs` library to find the appropriate path cross-platform) or the application's directory.
  * Provide default values if the config file is missing or invalid.
  * Persist any changes made via a potential (optional) settings UI back to the config file. Store the API key, location, units, font path, format strings.

## 6. Performance Requirements

* **Low CPU Usage:** The application should consume minimal CPU resources when idle (only updating the clock). CPU usage will spike briefly during weather updates.
* **Low Memory Footprint:** Keep memory usage reasonable.
* **UI Responsiveness:** The UI must remain responsive at all times. Network requests (weather lookup) must not freeze the UI.
* **Fast Startup:** The application should launch quickly.

## 7. Error Handling

* Handle network errors during API calls gracefully (e.g., display "N/A" or "Error" for weather, log the error).
* Handle invalid API responses or missing data.
* Handle invalid configuration (e.g., location not found by API, invalid font path). Display informative messages to the user.
* Handle missing API key - prompt user or display placeholder data.

## 8. Packaging (Optional)

* Provide instructions or a script using `PyInstaller` to create a single-file or single-directory executable for Windows, macOS, and Linux. Ensure necessary assets (fonts, icons, config template) are bundled correctly.

## 9. Future Enhancements (Optional)

* Basic settings UI instead of manual config file editing.
* Multiple location support.
* Forecast display (e.g., next few hours/days).
* More detailed weather info (humidity, wind speed, feels-like).
* Click-through window option.
* Auto-location detection (using OS location services or IP geolocation).
