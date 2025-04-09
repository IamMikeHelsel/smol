#!/usr/bin/env python3
"""
Alternative launcher script for PyWeatherClock
"""

import os
import sys

# Add the current directory to the Python path to ensure modules can be found
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Execute the main module directly
print("Starting PyWeatherClock...")
exec(open("pyweatherclock.py").read())
