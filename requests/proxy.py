import requests

# Step 1: Define proxies dictionary
proxies = {
    'http': '172.67.70.71:80',
    # 'https': '202.159.35.97:443',
}

# Step 2: Make a GET request through the proxy
r = requests.get('https://httpbin.org/ip', proxies=proxies)

# Step 3: Print the response text to verify the origin IP
print(r.text)
