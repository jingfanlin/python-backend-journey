import requests

url = "http://127.0.0.1:5000/status"
data = {"status": "focus"}

resp = requests.post(url, json=data)
print(resp.status_code)
print(resp.json())