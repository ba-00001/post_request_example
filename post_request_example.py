#post_request_example.py
import requests

def send_post_request():
    # URL for the API endpoint
    url = "https://jsonplaceholder.typicode.com/posts"

    # Data to be sent in the POST request
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    # Sending the POST request
    response = requests.post(url, json=payload)

    # Checking if the request was successful
    if response.status_code == 201:
        print("POST request successful!")
        print("Response JSON:")
        print(response.json())
    else:
        print("POST request failed!")
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")

if __name__ == "__main__":
    send_post_request()

def send_get_request():
    # URL for the API endpoint
    url = "https://jsonplaceholder.typicode.com/posts/1"

    # Sending the GET request
    response = requests.get(url)

    # Checking if the request was successful
    if response.status_code == 200:
        print("GET request successful!")
        print("Response JSON:")
        print(response.json())
    else:
        print("GET request failed!")
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")

if __name__ == "__main__":
    send_get_request()

