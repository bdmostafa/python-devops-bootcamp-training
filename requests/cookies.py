import requests

# 1️⃣ Set the target URL
url = "https://httpbin.org/cookies"

# 2️⃣ Simulate a user location cookie
cookies = {
    "location": "Dhaka"
}

# Send a GET request with custom cookies
response = requests.get(url, cookies=cookies)
print("🔹 Sending Cookies to Server:")
print(response.text)


# 3️⃣ Receive cookies from a real server (Google)
print("\n🔹 Receiving Cookie from Google:")
r2 = requests.get("https://www.google.com")

# Access a specific cookie (may vary by region/device)
if '1P_JAR' in r2.cookies:
    print("1P_JAR Cookie Value:", r2.cookies['1P_JAR'])
else:
    print("❌ '1P_JAR' cookie not found. Try a different cookie name or site.")


# 4️⃣ Advanced: Using RequestsCookieJar for domain/path-specific cookies
from requests.cookies import RequestsCookieJar

# Create a custom cookie jar
jar = RequestsCookieJar()

# Add cookie with domain/path set to match request
jar.set('userId', 'John99', domain='httpbin.org', path='/cookies')
jar.set('cartItem', 'laptop', domain='httpbin.org', path='/cart')

# Make request to /cookies (only userId should appear)
r3 = requests.get("https://httpbin.org/cookies", cookies=jar)
print("\n🔹 Custom CookieJar - /cookies path:")
print(r3.text)

# Make request to /cart (only cartItem should appear)
r4 = requests.get("https://httpbin.org/cart", cookies=jar)
print("\n🔹 Custom CookieJar - /cart path:")
print(r4.text)
