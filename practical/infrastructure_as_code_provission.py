import requests

headers = {
    "Authorization": "Bearer <API_TOKEN>",
    "Content-Type": "application/json"
}
droplet_data = {
    "name": "devops-droplet",
    "region": "nyc3",
    "size": "s-1vcpu-1gb",
    "image": "ubuntu-20-04-x64"
}
response = requests.post("https://api.digitalocean.com/v2/droplets", headers=headers, json=droplet_data)
print(response.json())
