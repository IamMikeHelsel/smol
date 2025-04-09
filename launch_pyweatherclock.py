#!/usr/bin/env python3
"""
Ultra-simple launcher for PyWeatherClock with maximum compatibility
"""

import os
import sys
import traceback

try:
    # Change to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # Add the current directory to the Python path
    if script_dir not in sys.path:
        sys.path.insert(0, script_dir)

    # Print diagnostic information
    print(f"Python version: {sys.version}")
    print(f"Current directory: {os.getcwd()}")
    print(f"Script directory: {script_dir}")
    print(f"sys.path: {sys.path}")

    # Try importing and running
    print("Starting PyWeatherClock...")
    import pyweatherclock
    pyweatherclock.main()

except Exception as e:
    print("\n===== ERROR =====")
    print(f"Error running PyWeatherClock: {e}")
    print("\nDetailed traceback:")
    traceback.print_exc()

    print("\n===== TROUBLESHOOTING =====")
    print("1. Make sure you have installed all dependencies:")
    print("   pip install -r requirements.txt")
    print("2. Make sure you're running this script from the PyWeatherClock directory")
    print("3. Check if all required files and directories exist:")

    required_paths = [
        "pyweatherclock.py",
        "utils/config_manager.py",
        "utils/weather_api.py",
        "ui/clock_widget.py"
    ]

    for path in required_paths:
        full_path = os.path.join(script_dir, path)
        exists = os.path.exists(full_path)
        print(f"   - {path}: {'✓' if exists else '✗'}")
        if not exists:
            print(f"     Full path: {full_path}")

    print("\n4. Check sys.path to ensure the application directory is included.")
    print("5. Verify that the PYTHONPATH environment variable is not interfering.")

    input("\nPress Enter to exit...")
    sys.exit(1)
