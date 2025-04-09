#!/usr/bin/env python3
"""
Reliable launcher script for PyWeatherClock with enhanced error handling
"""

import os
import sys
import traceback

def check_dependencies():
    """Check for required dependencies with helpful error messages"""
    missing_deps = []
    
    try:
        import customtkinter
    except ImportError:
        missing_deps.append("customtkinter>=5.2.0")
    
    try:
        from PIL import Image, ImageTk
    except ImportError:
        missing_deps.append("pillow>=9.0.0")
    
    try:
        import requests
    except ImportError:
        missing_deps.append("requests>=2.28.0")
    
    try:
        import appdirs
    except ImportError:
        missing_deps.append("appdirs>=1.4.4")
    
    if missing_deps:
        print("ERROR: Missing required dependencies:")
        for dep in missing_deps:
            print(f"  - {dep}")
        print("\nPlease install them with:")
        print(f"pip install {' '.join(missing_deps)}")
        return False
    
    return True

def main():
    """Launch PyWeatherClock with enhanced error handling"""
    # Ensure we're in the correct directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Add the current directory to sys.path
    if script_dir not in sys.path:
        sys.path.insert(0, script_dir)
    
    # Check dependencies first
    if not check_dependencies():
        sys.exit(1)
    
    # Check for necessary files
    required_files = [
        "pyweatherclock.py",
        os.path.join("utils", "config_manager.py"),
        os.path.join("utils", "weather_api.py"),
        os.path.join("ui", "clock_widget.py")
    ]
    
    for file_path in required_files:
        if not os.path.exists(file_path):
            print(f"ERROR: Required file not found: {file_path}")
            print("Make sure you're running this script from the PyWeatherClock directory.")
            sys.exit(1)
    
    try:
        print("Starting PyWeatherClock...")
        # Import the module
        import pyweatherclock
        
        # Run the application
        pyweatherclock.main()
    except ImportError as e:
        print(f"ERROR: Failed to import PyWeatherClock: {e}")
        print("This might be due to missing dependencies or incorrect file structure.")
        print("Make sure all the required files are present and all dependencies are installed.")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Failed to run PyWeatherClock: {e}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
