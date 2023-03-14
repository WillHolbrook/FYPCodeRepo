from pathlib import Path
import requests

def upload_report(file_path: Path):
    url = "http://willholbrook.com/api/report_upload/"

    payload = {}
    files = [
        ('uploaded_report', (file_path.name, open(file_path, 'rb'), 'application/pdf'))
    ]
    headers = {
        'Authorization': 'Token 868a9296111911d1865ec562e069a4f3e7a60696'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)


# Set the directory path
dir_path = Path('./validated-reports')

# Walk through all the files in the directory
for file_path in dir_path.glob('*.pdf'):
    if file_path.is_file():
        # Call the function on the file
        upload_report(file_path)
