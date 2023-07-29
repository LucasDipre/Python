import requests

#Criando um repositório no github via api com requsisção POST
# especificando a versão da API
api_base_url = 'https://api.github.com'
url = f'{api_base_url}/user/repos'
access_token = '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'
headers = {'Authorization' : 'Bearer ' + access_token, 'X-GitHub-Api-Version': '2022-11-28'}

data = {
    'name': 'linguagens-utilizadas',
    'description': 'Repositorio com as linguagens de prog da Amazon',
    'private': False
}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)