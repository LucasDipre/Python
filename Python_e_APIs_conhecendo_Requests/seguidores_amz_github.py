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


# criando uma lista vazia
followers_name = []

# # percorrendo a lista com os dados dos seguidores e selecionando apenas o nome de usuário
# for page in followers_list:
#     for follower in page:
#         followers_name.append(follower['login'])

# conferindo o tamanho da lista
print(len(followers_name))

