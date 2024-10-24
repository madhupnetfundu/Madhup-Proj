import requests 
from requests.auth import HTTPBasicAuth 
from getpass import getpass

# Making a get request 
# response = requests.get('https://api.github.com/user', 
# 			auth = HTTPBasicAuth('madhupnetfundu', 'Sungard0@'))

url = 'https://api.github.com/user'

requests.get(url, auth=('madhupnetfundu', getpass()), timeout=10)
