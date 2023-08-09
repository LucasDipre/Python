#Respondendo a pergunta do curso, coloquei o código para rodar
subst = "Python"
verbo = "é"
adjetivo = "fantástico"
print(subst, verbo, adjetivo, sep="_", end="!\n")

#Desafio do curso para imprimir datas
dia = 15
mes = 10
ano = 2015
#Resultado meu
print(dia, mes, ano, sep="/")

#Desafio Curso, Qual o tipo da variável?
preco = 49.99
#Resultado meu
tipo_preco = type(preco)
print(tipo_preco)

#O Python utiliza por convenção o padrão Snake_Case para nomes de variáveis (ou identificadores).
idade_esposa = 20
perfil_vip = 'Flávio Almeida'
recibos_em_atraso = 30

#Teste do curso 
numero1 = 10
numero2 = 10
if(numero1 == numero2): #o erro era que precisa ser == para comparar com if
    print("São números iguais")

#teste do curso resolve-se usando a funcao int
idade1 = 10
idade2 = int("20")
print(idade1 + idade2)

#Teste do curso para ver se o aluno prestou atenção no uso do : após o if
minha_idade = 26
idade_namorado = 25
if(minha_idade == idade_namorado):
    print('temos idades iguais')
else:
    print('temos idades diferentes')

# Oque acontece Quando o usuário digitar 12, o que será mostrado no console?
idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if (idade > 18):
    print("Você é maior de idade.")
else:
    if (idade < 12):
        print("Você é uma criança.")
    elif (idade > 12):
        print("Você é um adolescente.")

#Quando o usuário digitar 12, nenhuma condição será satisfeita! Repare que:
#12 não é maior que 18 (idade > 18).
#12 não é menor que 12 (idade < 12).
#12 não é maior que 12 (idade > 12).
#É preciso testar a igualdade através do ==.
#Saiba também, que além do == (igualdade), > (maior) e < (menor), também temos >= (maior ou igual), <= (menor ou igual) e != (diferente).

#Desafio idade para usar tipos diferente de comparadores
idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if (idade >= 18):
    print("Você é maior de idade.")
else:
    if (idade < 12):
        print("Você é uma criança.")
    elif (idade >= 12):
        print("Você é um adolescente.")

#Desafio idade 
idade_str = input("Digite sua idade: ")
idade = int(idade_str)

maior_idade = idade > 18
print(maior_idade)
crianca     = idade < 12
print(crianca)
adolescente = idade > 12
print(adolescente)

#Desafio sistema de identificação de usuários ,resolvido trocando os else por elif
usuario = input("Informe o usuário do sistema!")

if(usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
elif(usuario == "Douglas"):
    print("Seja bem-vindo Douglas!")
elif(usuario == "Nico"):
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!")


#Apenas olhando este código, sem executá-lo, qual será a saída no console?

contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 2
    if(contador == 5):
        contador = contador + 2

# Resposta:
# 1
# 3
# 7
# 9

# i = 5 não vai funcionar pois será subescrito por conta do do proximo indice do range 
for i in range(10):
    print(i)
    i = 5

#Introdução do tipo bool
existe = True
type(existe)
