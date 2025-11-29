import requests  # Import the requests module to send HTTP requests

try:
    # Ask the user to input a URL
    url = input("Enter the url:\n")

    # Send a GET request to the given URL with a timeout of 3 seconds
    # If the site does not respond within 3 seconds, a Timeout exception is raised
    # response = requests.get("https://google.com")  # Example (commented)
    response = requests.get(url, timeout=3)

    # Print the HTTP status code returned by the server
    print(response.status_code)

# This will run if the URL is wrong or internet connection fails
except requests.exceptions.ConnectionError:
    print("Error due to the wrong url or connection failed!")

# This will run if the request takes more than 3 seconds
except requests.exceptions.Timeout:
    print("Time out!")

# This will catch any other unexpected errors
except Exception as e:
    print(e)


