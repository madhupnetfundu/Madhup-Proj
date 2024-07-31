import requests

from requests.exceptions import ConnectionError

url = 'https://httpbin1.org' ## note the website name is chosen as httpbin1.org instead of httpbin.org

try:
    response = requests.get(url, timeout=0.5)
except ConnectionError as ce:
    print(f'You got a connection error, check this out :\n{ce}')
except Exception as err:
    print(f'You got a boo boo:\n{err}')
else:
    print("the website works")