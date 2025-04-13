import requests

# Step 1: Create a session object
s = requests.Session()

# Step 2: Define the cookies you want to set
userName = {"userName": "Mostafa"}
location = {"location": "Dhaka"}

# Step 3: Define the URLs
setCookieUrl = "https://httpbin.org/cookies/set"
getCookiesUrl = "https://httpbin.org/cookies"

# Step 4: Set the cookies via GET requests with params
s.get(setCookieUrl, params=userName)
s.get(setCookieUrl, params=location)

# Step 5: Get the current cookies from the server
r = s.get(getCookiesUrl)

# Step 6: Print the response text
print(r.text)
