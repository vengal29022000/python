import requests

url = f'https://api.github.com/repos/iam-veeramalla/python-for-devops/pulls'

response = requests.get(url)

if response.status_code == 200:
    # Convert the JSON response to a dictionary
    pull_requests = response.json()