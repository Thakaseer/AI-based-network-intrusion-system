#!/usr/bin/env python3
"""
Quick start script for AI Network Intrusion Detection System
"""

import os
import sys
import subprocess
import platform

def print_header(text):
    """Print formatted header"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")

def check_python_version():
    """Check Python version"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("Error: Python 3.8+ required")
        sys.exit(1)
    print(f"✓ Python {version.major}.{version.minor}.{version.micro}")

def install_dependencies():
    """Install required dependencies"""
    print_header("Installing Dependencies")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("\n✓ Dependencies installed successfully")
    except subprocess.CalledProcessError:
        print("\n✗ Failed to install dependencies")
        sys.exit(1)

def train_models():
    """Train models"""
    print_header("Training Models")
    
    try:
        subprocess.check_call([sys.executable, "train.py"])
        print("\n✓ Models trained successfully")
    except subprocess.CalledProcessError:
        print("\n✗ Failed to train models")
        sys.exit(1)

def run_demo():
    """Run demo detection"""
    print_header("Running Demo Detection")
    
    try:
        subprocess.check_call([sys.executable, "detect.py", "--mode", "demo"])
    except subprocess.CalledProcessError:
        print("\n✗ Demo failed")
        sys.exit(1)

def run_web_server():
    """Run web server"""
    print_header("Starting Web Server")
    
    print("Web server starting at http://localhost:5000")
    print("Press Ctrl+C to stop\n")
    
    try:
        subprocess.check_call([sys.executable, "detect.py", "--mode", "api"])
    except KeyboardInterrupt:
        print("\n✓ Web server stopped")

def main():
    """Main entry point"""
    print_header("AI Network Intrusion Detection System - Quick Start")
    
    # Check Python version
    print("Checking Python version...")
    check_python_version()
    
    # Menu
    print("\nSelect an option:")
    print("1. Install dependencies")
    print("2. Train models")
    print("3. Run demo detection")
    print("4. Start web server")
    print("5. Full setup (1 + 2 + 3)")
    print("6. Exit")
    
    choice = input("\nEnter your choice (1-6): ").strip()
    
    if choice == "1":
        install_dependencies()
    elif choice == "2":
        train_models()
    elif choice == "3":
        run_demo()
    elif choice == "4":
        run_web_server()
    elif choice == "5":
        install_dependencies()
        train_models()
        run_demo()
    elif choice == "6":
        print("\nGoodbye!")
        sys.exit(0)
    else:
        print("\nInvalid choice")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)
