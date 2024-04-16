import requests

try:
    # Specify the URL you want to make a GET request to
    # url = 'https://google.com'
    url = 'https://1.2.3.4.com'

    # Make the GET request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the response content
        print(response.text)
    else:
        # Print an error message if the request was not successful
        print('Error:', response.status_code)

except requests.exceptions.ConnectionError as e:
    # Handle any exceptions that occur during the request
    # print('An error occurred during the request:', e)
    print('An error occurred during the request: ConnectionError')