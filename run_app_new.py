#!/usr/bin/env python3
"""
Updated launcher script for PyWeatherClock
"""

import os
import sys

# Add the current directory to the Python path to ensure modules can be found
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Now import and run the main application
try:
    print("Starting PyWeatherClock...")
    # Use a direct path approach
    import pyweatherclock as pwc
    
    app = pwc.PyWeatherClock()
    print("PyWeatherClock initialized, running main loop...")
    app.run()
except Exception as e:
    import traceback
    print(f"Error running PyWeatherClock: {e}")
    traceback.print_exc()
    sys.exit(1)
