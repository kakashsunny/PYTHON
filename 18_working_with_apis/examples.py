# Working with APIs Examples and Practice
import requests

# 1. Making a safe GET request with timeouts and exception handling
def fetch_mock_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    try:
        # 5 second timeout
        response = requests.get(url, timeout=5)
        # Raises HTTPError if status code is 4xx/5xx
        response.raise_for_status() 
        
        data = response.json()
        print("Fetched post title:", data.get("title"))
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
    return None

fetch_mock_data()

# 2. Making a POST request
def create_mock_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "Learning Python API Calls",
        "body": "This is a post created via the requests library.",
        "userId": 1
    }
    try:
        response = requests.post(url, json=payload, timeout=5)
        print("POST Status Code:", response.status_code)
        print("Response JSON:", response.json())
    except Exception as e:
        print("Post failed:", e)

create_mock_post()
