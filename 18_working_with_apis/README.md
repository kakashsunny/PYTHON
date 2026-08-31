# Working with APIs in Python

## Definitions & Concepts
An Application Programming Interface (API) allows two software applications to communicate. Most web APIs use HTTP protocols to exchange data in JSON format.

## Core HTTP Methods
- **GET**: Retrieve data.
- **POST**: Send data to create a new resource.
- **PUT/PATCH**: Update existing resources.
- **DELETE**: Delete resources.

## Python's `requests` Library
`requests` is the standard Python package used to make HTTP requests cleanly and efficiently.

## Syntax & Examples
```python
import requests

# Making a GET request
response = requests.get("https://api.github.com")

if response.status_code == 200:
    data = response.json()
    print(data["current_user_url"])
```

## Best Practices
- Always check the HTTP status code (e.g., `200` for OK, `404` for Not Found, `500` for Server Error).
- Set standard timeouts for requests (e.g. `requests.get(url, timeout=5)`) to prevent applications from hanging forever.
- Use environment variables to store sensitive information like API tokens/keys.

## Common Mistakes
- Forgetting to handle request errors (like network failures or bad URLs), causing script crashes. Use `try-except` blocks.
- Not closing sessions when performing multiple requests to the same server.

## Interview Tips
- **Q**: What is the difference between `response.text` and `response.json()`?
- **A**: `response.text` returns the raw content of the response as a unicode string. `response.json()` parses the JSON content into a Python dictionary or list, raising a `JSONDecodeError` if the response content is not valid JSON.
