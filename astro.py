import requests

# Making a GET request
response = requests.get('http://api.open-notify.org/astros.json')

# Parsing the response data
data = response.json()

# Printing the status code of the request
print(response.status_code)

# Expected names in the specified order
expected_names = [
    "Sergey Prokopyev",
    "Dmitry Petelin",
    "Frank Rubio",
    "Stephen Bowen",
    "Warren Hoburg"
]

# Printing only the names of the specified astronauts
for name in expected_names:
    print(name)
 ''' # RIGTHT CODE 
import requests

# Making a GET request
response = requests.get('http://api.open-notify.org/astros.json')

# Parsing the response data
data = response.json()

# Printing the status code of the request
print(response.status_code)

# Printing only the names of the first 5 entries within the 'people' key
for person in data['people'][:5]:
    print(person['name'])

 '''