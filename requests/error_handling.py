import requests

# Example 1: Handling HTTP error codes
try:
    r = requests.get("https://httpbin.org/status/404")
    r.raise_for_status()  # This will raise HTTPError for 4xx or 5xx responses
except requests.exceptions.HTTPError as err:
    print("❌ HTTP error occurred:", err)

# Example 2: Handling timeout
try:
    r = requests.get("https://httpbin.org/delay/2", timeout=0.1)
except requests.exceptions.Timeout as err:
    print("⌛ Timeout error occurred:", err)

# Good practice: Catch-all for any other request errors
except requests.exceptions.RequestException as err:
    print("⚠️ Other error occurred:", err)
