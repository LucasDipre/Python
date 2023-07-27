import requests

username = 'amzn'
url = f"https://api.github.com/users/{username}/followers"

# definindo o token e a versão da API
access_token = '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'
headers = {'Authorization': 'Bearer ' + access_token,
           'X-GitHub-Api-Version': '2022-11-28'}

page = 1
followers_list = []

while True: 

    # faz a requisição 
    url_page = f'{url}?page={page}'
    response = requests.get(url_page, headers=headers)

    # converte a resposta para um objeto JSON
    followers = response.json()

    # caso a lista esteja vazia, podemos sair do laço pois todos os dados foram extraidos
    # OU SEJA CHEGOU NA ULTIMA PAGINA COM ZERO SEGUIDORES
    if len(followers)==0:
        break

    # adicionando os seguidores a lista
    followers_list.append(followers)

    # incrementa o valor de 'page' para a próxima requisição
    page += 1

#print(len(followers_list))
print(*followers_list)