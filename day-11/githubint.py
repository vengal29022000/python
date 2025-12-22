import requests

url = f'https://api.github.com/repos/iam-veeramalla/python-for-devops/pulls'

response = requests.get(url)