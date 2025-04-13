import requests

# Default behavior: Redirection is followed
r = requests.get("http://github.com/")
print("Final URL after redirect:", r.url)
print("Final status code:", r.status_code)
print("History:", r.history)

# Disable redirection
r_no_redirect = requests.get("http://github.com/", allow_redirects=False)
print("\nWithout Redirection:")
print("URL:", r_no_redirect.url)
print("Status Code:", r_no_redirect.status_code)
print("History:", r_no_redirect.history)

# HEAD request with redirection allowed
r_head = requests.head("http://github.com/", allow_redirects=True)
print("\nHEAD Request Final URL:", r_head.url)
print("HEAD Request History:", r_head.history)
