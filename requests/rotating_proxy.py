import requests
import random

# list of free proxies (replace with actual working proxies)
PROXY_LIST = [
    "http://84.201.188.6:3128",
    "http://149.28.44.246:10041",
    "http://98.172.140.76:8080",
]


# randomly select a proxy from the list
def get_random_proxy():
    return random.choice(PROXY_LIST)


# get a random proxy
proxy = get_random_proxy()

# target url to check our IP
url = "https://httpbin.io/ip"

# make a request using the selected proxy
response = requests.get(url, proxies={"http": proxy, "https": proxy})

# print the response, which should show the proxy's IP
print(response.text)
