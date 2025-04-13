# https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Type

import requests

headers = {
    "Content-Type": "application/json"    
}

r = requests.post("https://httpbin.org/post", headers=headers)
print(r.json())
print(r.headers)
print(r.request.headers)
print(r.headers['Content-Type'])