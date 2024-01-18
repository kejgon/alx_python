import requests
import sys

# Retrieve command-line arguments
url = sys.argv[1]  # Adjust URL based on server environment
email = sys.argv[2]

# Send the POST request with the email as a parameter
try:
    response = requests.post(url, data={"email": email})
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print("Error: Could not connect to server. Please check server status and network connectivity.")
    print(f"Error details: {e}")
