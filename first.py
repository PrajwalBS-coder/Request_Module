import requests
url = 'https://jsonplaceholder.typicode.com/todos/1'
response = requests.get(url)
# Handling the response object
if response.status_code == 200:
    print('Request successful!')
    print('Response Content:', response.json())
else:
    print('Request failed with status code:', response.status_code)
    