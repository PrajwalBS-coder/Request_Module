import requests
url = 'https://github.com/harshadvali11/complete_wheather_app/blob/main/app/views.py'
response = requests.get(url)
# Handling the response object
if response.status_code == 200:
    print('Request successful!')
    print('Response Content:', response.headers())
else:
    print('Request failed with status code:', response.status_code)