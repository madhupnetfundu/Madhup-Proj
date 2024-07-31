# import requests module 
import requests 
from requests.auth import HTTPBasicAuth 

# Making a get request 
response = requests.get('https://httpbin.org', auth = HTTPBasicAuth('madhups', 'abc'))

# print request object 
print(response) 

## Replace “user” and “pass” with your username and password. It will authenticate the request and return a response 200 or else it will return error 403.

