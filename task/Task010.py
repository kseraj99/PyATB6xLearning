"""
Question 3 :
Simulate a page loading check using a while loop.
If page_loaded becomes True within 5 seconds, print success; else timeout.

Hint: Use a counter (like wait_time) and break c
"""

import time
import random

# Tracks how many seconds we have waited so far
wait_time = 0

# Will store whether the page is loaded (True/False)
page_loaded = False


# Function to simulate an API response (True = loaded, False = not loaded)
def api_response():
    # Randomly return True or False to simulate success/failure
    return random.choice([False, True])


# Try for a maximum of 5 seconds
while wait_time < 5:
    # Call the simulated API to check if the page is loaded
    page_loaded = api_response()

    if page_loaded:
        # If the page is loaded, immediately print success and exit loop
        print(f"✅ Page loaded successfully in {wait_time + 1} seconds.")
        break
    else:
        # If not loaded, print waiting message
        print(f"⏳ Checking... (second {wait_time + 1})")

        time.sleep(1)  # Wait for 1 second before retrying
        wait_time += 1  # Increase the wait time counter

# After loop finishes, check if page_loaded is still False
if not page_loaded:
    print("❌ Timeout! Page failed to load within 5 seconds.")
