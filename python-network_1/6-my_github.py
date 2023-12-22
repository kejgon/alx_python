import requests
import sys

if len(sys.argv) != 3:
    print("Usage: {} <kejgon> <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>".format(sys.argv[0]))
    sys.exit(1)

username = sys.argv[1]
token = sys.argv[2]

url = "https://api.github.com/user"
headers = {'Authorization': 'Basic ' + '{}:{}'.format(username, token).encode('base64')}

try:
    response = requests.get(url, headers=headers)
    user_data = response.json()
    print(user_data.get('id', 'None'))
except ValueError:
    print('None')
