import requests

tests = ["tired", "ghost", "232421"]  # 200 / 404 / 400

for status in tests:
    url = f"http://127.0.0.1:5000/status/{status}"
    r = requests.get(url)
    print("\n==>", url)
    print("code:", r.status_code)
    print("json:", r.json())