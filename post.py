import requests

# Data to be sent in the POST request
data = {
    'title': 'Special Agent',
    'body': 'Leroy Jethro Gibbs',
    'userId': '1'
}

# Sending the POST request
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)

# Printing out the status code of the response
print(response.status_code)

# Printing out the response
print(response.json())
