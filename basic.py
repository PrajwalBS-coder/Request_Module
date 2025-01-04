import requests
# r = requests.get('https://api.github.com/events')
# print(r.cookies)
payload = {'Name': 'Jhon', 'Password': 'Prajwal'}
r = requests.get('https://httpbin.org/get', params=payload)
# print(r.text)
print(r.encoding)
r.encoding = 'ISO-8859-1'
print(r.text)
print(r.encoding)
from PIL import Image
from io import BytesIO

# i = Image.open(BytesIO(r.content))
# print(i)
print(r.content)