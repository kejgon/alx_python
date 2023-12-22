#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: {} <URL> <email>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Ensure there is a slash between the URL and the email parameter
if url.endswith('/'):
    url += 'withemail=' + email
else:
    url += '/withemail=' + email

payload = {'email': email}
response = requests.post(url, data=payload)

print("Your email is: {}".format(email))
print(response.text)
