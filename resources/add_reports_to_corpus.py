import requests

url = "http://localhost:8030/api/reports/"

payload={}
headers = {
  'Authorization': 'Token 27e71b26d075711968976e2bb548600b746ef896'
}

response = requests.request("GET", url, headers=headers, data=payload)

report_list = response.json()

for report in report_list:
    url = f"http://localhost:8030/api/add_to_corpus/{report['pk']}/"
    print(url)
    response = requests.request("POST", url, headers=headers, data=payload)
