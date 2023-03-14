import requests

url = "http://localhost:8030/api/calculate_idf/"

payload={}
headers = {
  'Authorization': 'Token e917246783466952173a919f4f9bf2e6f728638f'
}

response = requests.request("POST", url, headers=headers, data=payload, timeout=(60*60))

print(response.text)
