import requests

url = "https://api.github.com/repos/<username>/<repo>/dispatches"
headers = {
    "Authorization": "token YOUR_TOKEN",
    "Accept": "application/vnd.github+json"
}
data = {"event_type": "build"}
r = requests.post(url, headers=headers, json=data)
print(r.json())