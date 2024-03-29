from pathlib import Path
import requests


def upload_report(file_path: Path):
    # print(file_path)
    url = "http://localhost:8030/api/report_upload/"

    payload = {}
    files = [
        ('uploaded_report', (file_path.name, open(file_path, 'rb'), 'application/pdf'))
    ]
    headers = {
        'Authorization': 'Token 4331cec7ce201eee0fa0a1f6d13a7e4673c954a2'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    if response.status_code != 200:
        print(file_path)
        print(response.text)
        print(response.status_code)


# Set the directory path
dir_path = Path('../../datasets/validated-gold-reports')
i = 0

# Walk through all the files in the directory
for file_path in dir_path.glob('*.pdf'):
    print(file_path)
    if file_path.is_file():
        # if i < 10:
            # Call the function on the file
        upload_report(file_path)
        i += 1
        print(i)
        # else:
        #     break
