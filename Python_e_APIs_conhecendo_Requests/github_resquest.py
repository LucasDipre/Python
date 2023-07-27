import requests

# especificando a versão da API
api_base_url = 'https://api.github.com'
owner = 'amzn' # username de quem vamos extrair os dados
url = f'{api_base_url}/users/{owner}/repos'
access_token = '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'
headers = {'Authorization': 'Bearer' + access_token,
           'X-GitHub-Api-Version': '2022-11-28'}
           

response = requests.get(url, headers=headers)

repos_list = []
for page_num in range(1, 6):
    try:
        url_page = f'{url}?page={page_num}'
        response = requests.get(url_page, headers=headers)
        repos_list.append(response.json())
    except:
        repos_list.append(None)

print(len(repos_list))
print(len(repos_list[0]))
print(len(repos_list[1]))
print(len(repos_list[2]))


