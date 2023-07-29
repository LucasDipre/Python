import base64
import requests

with open('amazon.csv', 'rb') as file:
    file_content = file.read()

encoded_content = base64.b64encode(file_content)

access_token = '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'
headers = {'Authorization': 'Bearer' + access_token,
           'X-GitHub-Api-Version': '2022-11-28'}

api_base_url = 'https://api.github.com'
username = 'LucasDipre'
repo = 'linguagens-utilizadas'
path = 'amazon.csv'

url = f'{api_base_url}/repos/{username}/{repo}/contents/{path}'

data = {
    'message': 'Adicionando um novo arquivo',
    'content': encoded_content.decode('utf-8')
}

response = requests.put(url, json=data, headers=headers)
print(response.status_code)
