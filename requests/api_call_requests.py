import requests

# response = requests.get("https://api.example.com/data")  
# print(response.json())  


# GET Example:
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.json())


# POST Example:
data = {"title": "DevOps", "body": "Automation is life", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print(response.status_code)


# Auth Example:
# response = requests.get("https://api.github.com/user", auth=("username", "token"))


# GET request with query parameters
r1 = requests.get("https://httpbin.org/get", params={'name': 'DevOps', 'course': 'Python'})
print("🔹 GET Response:")
print(r1.json())

# POST request with form data
payload = {'username': 'mostafa', 'password': 'devops123'}
r2 = requests.post("https://httpbin.org/post", data=payload)
print("\n🔹 POST Response:")
print(r2.json())


# Fetch Public IP Using API
def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        print(response.json())
        if response.status_code == 200:
            data = response.json()
            print(f"🌐 Your public IP is: {data['ip']}")
        else:
            print(f"⚠️ API Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Failed to fetch IP: {e}")

get_public_ip()


