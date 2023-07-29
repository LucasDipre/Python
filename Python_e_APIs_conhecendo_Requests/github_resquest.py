import requests
import pandas as pd

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

repos_name = []
for page in repos_list:
    for repo in page:
        repos_name.append(repo['name'])

# [ # lista 

#     [ # sublista 
#         {repositorio_1}, # dicionários
#         {repositorio_2}
#     ],

#     [ # sublista
#         {repositorio_3}, # dicionarios
#         {repositorio_4}
#     ]

# ]

print(repos_list[1][1]['language'])

repos_language = []
for page in repos_list:
    for repo in page:
        repos_language.append(repo['name'])

print(len(repos_language))
print(repos_language)
# print(len(repos_name))
# print(repos_name)

#Criando um dataframe  e criando duas colunas em uma tabela no dataframe
dados_amz = pd.DataFrame()
dados_amz['repository_name'] = repos_name
dados_amz['language'] = repos_language

print(dados_amz)

#Gerando um .csv com os dadso do dataframe
dados_amz.to_csv('amazon.csv')
