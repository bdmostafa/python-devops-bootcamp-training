import requests

r = requests.get("https://api.github.com/events")
data = r.json()
print(data[0])
print(data[0]['actor'])
print(data[0]['actor']['login'])

payload = {'key1': 'value1', 'key2': 'value2'}
r2 = requests.post("https://httpbin.org/post", data=payload) 
print(r2.text)