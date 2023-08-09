# Romeu e seus colegas estavam competindo em um campeonato de futebol com 
# o seu time 'Drible da emoção'.

# Como ele era um dos organizadores, tinha de manter a colocação de cada 
# um dos 4 times manualmente, levando em consideração diversos fatores 
# como número de pontos, gols marcados e etc... Como Romeu era um estudante 
# de Ciências da Computação, ele resolveu automatizar este processo todo 
# em um script em Python, para facilitar sua vida e dedicar mais tempo aos treinos.

# O seu script funcionou maravilhosamente bem, porém no dia de entrega dos 
# resultados ele percebeu um erro. O script gerava a lista de colocação corretamente, 
# porém na hora de exibir o resultado final com o campeão, ele sempre mostrava o 
# segundo colocado em vez do primeiro colocado na Lista.

## Restante do código que gera a lista de colocação...
colocacao = ['Drible da Emoção', 'Bruxos como Ronaldinho', 'Só golaço', '3x1 não é goleada']


print(colocacao)
#Resultado: ['Drible da Emoção', 'Bruxos como Ronaldinho', 'Só golaço', '3x1 não é goleada']

campeao = colocacao[1]

print(' O grande campeão do torneio é o time ' + campeao)
#Resultado:  O grande campeão do torneio é o time Bruxos como Ronaldinho

# Aponte o provável erro de Romeu na hora de exibir o primeiro colocado de sua lista, 
# para que o seu time Drible da Emoção seja devidamente coroado campeão.

#resposta
campeao = colocacao[0]