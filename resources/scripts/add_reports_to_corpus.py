import requests

url = "http://localhost:8030/api/reports/"

payload={}
headers = {
  'Authorization': 'Token 27e71b26d075711968976e2bb548600b746ef896'
}

response = requests.request("GET", url, headers=headers, data=payload)

report_list = response.json()
i = 0

print(report_list)

for report in report_list:
    url = f"http://localhost:8030/api/add_to_corpus/{report['pk']}/"
    # print(url)
    response = requests.request("POST", url, headers=headers, data=payload)
    i += 1
    print(i)

    if response.status_code != 200:
        print(report)
        print(response.text)
        print(response.status_code)
