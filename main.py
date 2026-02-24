import requests

response = requests.get("https://github.com")
print("Status Code:", response.status_code)