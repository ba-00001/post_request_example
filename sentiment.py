import requests

# URL for the Sentiment Analysis API
url = 'http://text-processing.com/api/sentiment/'

# Get text from the user
user_text = input("Enter the text you want to analyze: ")

# Prepare the data to be sent in the POST request
data = {'text': user_text}

# Send the POST request
response = requests.post(url, data=data)

# Print out the response
print(response.json())
