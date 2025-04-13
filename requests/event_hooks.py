import requests

# Step 1: Define the callback function
def response_info(r, *args, **kwargs):
    print(f"Status Code: {r.status_code}")
    print(f"URL: {r.url}")
    print(f"Response Body: {r.text}")

# Step 2: Define the hooks dictionary
hooks = {
    'response': response_info
}

# Step 3: Make a GET request and pass hooks
r = requests.get('https://httpbin.org/get', hooks=hooks)
print("🔹 Response:")
print(r.text)

# Step 4: 
def response_headers(r, *args, **kwargs):
    print(f"Response Headers: {r.headers}")
    
hooks2 = {
    'response': [response_info, response_headers]
}

# Step 5: Make a GET request and pass hooks
requests.get('https://httpbin.org/get', hooks=hooks2)