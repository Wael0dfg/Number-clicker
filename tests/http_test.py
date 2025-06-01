"""
Test script for Number Clicker application

This script tests the HTTP responses of the Number Clicker application.
"""

import requests
import sys

def test_application():
    """Test the Number Clicker application"""
    base_url = "http://localhost:8080"
    
    # Test 1: Check if the main page loads
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print("✅ Main page loads successfully")
            if "Number Clicker" in response.text:
                print("✅ Main page contains 'Number Clicker' title")
            else:
                print("❌ Main page does not contain 'Number Clicker' title")
                
            if "incrementNumber()" in response.text:
                print("✅ Main page contains increment function")
            else:
                print("❌ Main page does not contain increment function")
                
            if "decrementNumber()" in response.text:
                print("✅ Main page contains decrement function")
            else:
                print("❌ Main page does not contain decrement function")
                
            if "resetNumber()" in response.text:
                print("✅ Main page contains reset function")
            else:
                print("❌ Main page does not contain reset function")
                
            if "saveProgress()" in response.text:
                print("✅ Main page contains save function")
            else:
                print("❌ Main page does not contain save function")
                
            if "loadProgress" in response.text:
                print("✅ Main page contains load function")
            else:
                print("❌ Main page does not contain load function")
        else:
            print(f"❌ Main page failed to load with status code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error accessing main page: {str(e)}")
    
    # Test 2: Check if the help page loads
    try:
        response = requests.get(f"{base_url}/htu.html")
        if response.status_code == 200:
            print("✅ Help page loads successfully")
            if "How To Use Number Clicker" in response.text:
                print("✅ Help page contains 'How To Use Number Clicker' title")
            else:
                print("❌ Help page does not contain 'How To Use Number Clicker' title")
                
            if "goBackToMain()" in response.text:
                print("✅ Help page contains navigation function")
            else:
                print("❌ Help page does not contain navigation function")
        else:
            print(f"❌ Help page failed to load with status code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error accessing help page: {str(e)}")
    
    # Test 3: Check for CSS styling and modern design elements
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            if "linear-gradient" in response.text:
                print("✅ Main page contains gradient styling")
            else:
                print("❌ Main page does not contain gradient styling")
                
            if "animation" in response.text:
                print("✅ Main page contains animations")
            else:
                print("❌ Main page does not contain animations")
                
            if "backdrop-filter: blur" in response.text:
                print("✅ Main page contains glassmorphism effect")
            else:
                print("❌ Main page does not contain glassmorphism effect")
                
            if "@media screen and" in response.text:
                print("✅ Main page contains responsive design media queries")
            else:
                print("❌ Main page does not contain responsive design media queries")
        else:
            print(f"❌ Failed to check styling with status code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error checking styling: {str(e)}")

if __name__ == "__main__":
    test_application()
    print("\nTest completed!")