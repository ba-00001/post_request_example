# WRITE YOUR CODE HERE
import requests

# URL for the POST request
url = 'https://httpbin.org/post'

# Sending the POST request
response = requests.post(url)

# Printing out the response
print(response.json())
