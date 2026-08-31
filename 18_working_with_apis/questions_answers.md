# Questions & Answers: Working with APIs

## MCQs
1. **Which HTTP status code represents a successful resource creation?**
   - A) 200 OK
   - B) 201 Created
   - C) 400 Bad Request
   - D) 301 Moved Permanently
   - **Answer**: B
   - **Explanation**: 201 represents "Created", standard for successful POST requests.

2. **How do you handle request connection errors in python requests?**
   - A) Catch `requests.exceptions.ConnectionError`
   - B) Catch `ConnectionError` builtin
   - C) Raise `NetworkError`
   - D) Run `ping`
   - **Answer**: A
   - **Explanation**: `requests` packages its own connection exceptions inside `requests.exceptions`.

## Beginner & Intermediate Questions
### Q1: What does `response.raise_for_status()` do?
**Answer**: It checks if the HTTP status code of the response is an error (4xx or 5xx). If so, it raises an instance of `HTTPError`, allowing you to catch HTTP failures easily.

### Q2: What is the purpose of passing a headers dictionary to `requests.get()`?
**Answer**: Headers allow you to pass metadata about the request, such as authentication tokens (e.g. `Authorization: Bearer <TOKEN>`) or content type expectations (e.g. `Accept: application/json`).

## Coding Practice & Solutions
### Problem: Write a function to check if a website is online (returns a 200 status code within 3 seconds).
**Solution**:
```python
import requests

def is_website_online(url):
    try:
        response = requests.head(url, timeout=3)
        return response.status_code == 200
    except requests.RequestException:
        return False

print(is_website_online("https://www.google.com"))  # True
```
