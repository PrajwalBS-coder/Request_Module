import requests
# r = requests.get('https://api.github.com/events')
# print(r.cookies)
payload = {'Name': 'Jhon', 'Password': 'Prajwal'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.text)