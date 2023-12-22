#!/usr/bin/python3
import requests
import sys
import base64

if len(sys.argv) != 3:
    print("Usage: {} <username> <token>".format(sys.argv[0]))
    sys.exit(1)

username = sys.argv[1]
token = sys.argv[2]

# Combine username and token with a colon and encode in base64
credentials = base64.b64encode('{}:{}'.format(username, token).encode('utf-8')).decode('utf-8')

url = "https://api.github.com/user"
headers = {'Authorization': 'Basic ' + credentials}

try:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get('id', 'None'))
    else:
        print('None')
except ValueError:
    print('None')
