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
        'Authorization': 'Token 27e71b26d075711968976e2bb548600b746ef896'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    if response.status_code != 200:
        print(file_path)
        print(response.text)
        print(response.status_code)


# Set the directory path
dir_path = Path('../datasets/validated-reports')
i = 0

# Walk through all the files in the directory
for file_path in dir_path.glob('*.pdf'):
    if file_path.is_file():
        # if i < 10:
            # Call the function on the file
        upload_report(file_path)
        i += 1
        print(i)
        # else:
        #     break
