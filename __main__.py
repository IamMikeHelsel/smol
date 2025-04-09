"""
Main entry point for running PyWeatherClock as a module.
This allows running with: python -m pyweatherclock
"""

import sys
import os

# Add the parent directory to sys.path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Import and run the main function
try:
    from pyweatherclock import main
    main()
except ImportError:
    print("Error: Could not import PyWeatherClock. Make sure you're in the correct directory.")
    sys.exit(1)
except Exception as e:
    print(f"Error running PyWeatherClock: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
