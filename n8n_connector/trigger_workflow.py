import requests

from shared.constants import N8N_API_URL

def trigger_workflow():
    file_path = '../files/ads_spend.csv'

    with open(file_path, 'rb') as f:
        data = f.read()
    res = requests.post(url=N8N_API_URL,
                        data=data,
                        headers={'Content-Type': 'application/octet-stream'})

    print("Workflow triggered, response status code:", res.status_code)
    return res.status_code


if __name__ == "__main__":
    trigger_workflow()