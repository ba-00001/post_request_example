import requests
import os
import json
# Get client ID and secret from environment variables
CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

# Authentication URL
AUTH_URL = "https://accounts.spotify.com/api/token"

# Get access token
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# Parse the response to get the access token
auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']
headers = {'Authorization': f'Bearer {access_token}'}

# Base URL for Spotify API
BASE_URL = 'https://api.spotify.com/v1/'

# Get track ID from user input
track_id = input('Enter track id: ')

# Make a request to get audio features of the track
response = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)

# Print status code of the response
print(response.status_code)

# Print the data of the response
data = response.json()
print(data)
