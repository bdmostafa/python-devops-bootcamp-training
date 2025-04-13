import requests

query = 'up{job="node"}'
url = f"http://localhost:9090/api/v1/query?query={query}"
response = requests.get(url)
print(response.json())




