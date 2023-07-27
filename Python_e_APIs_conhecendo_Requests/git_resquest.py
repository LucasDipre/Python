import requests

r = requests.get('https://api.github.com/users/LucasDipre')

print(r.status_code)
# print(r.json)
# print(r.text)
print(r.url)

name = r.json()['name']

login = r.json()['login']

public_repos = r.json()['public_repos']

data_criacao = r.json()['created_at']

print(name)
print(login)
print(public_repos)
print(data_criacao)
