import requests

url = "http://localhost:8030/api/calculate_idf/"

payload={}
headers = {
  'Authorization': 'Token 27e71b26d075711968976e2bb548600b746ef896'
}

response = requests.request("POST", url, headers=headers, data=payload, timeout=(60*60))

print(response.text)
print(response.status_code)
print(response.headers)
