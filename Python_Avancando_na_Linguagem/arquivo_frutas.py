arquivo = open("palavras.txt", "w")
arquivo.write("banana\n")
arquivo.write("morango\n")
arquivo.write("melancia\n")
arquivo.write("maca\n")
arquivo.close()


arquivo = open("palavras.txt", "a")
arquivo.write("caja\n")
arquivo.write("laranja\n")
arquivo.close()

# #Percorre o arquivo imprimindo a linha
arquivo = open("palavras.txt", "r")
# arquivo.read()
for linha in arquivo:
    print(linha.strip())

# # Lê apenas uma linha do arquivo
arquivo = open("palavras.txt", "r")
linha = arquivo.readline()
print(type(linha))
print(linha)

#imprimindo o arquivo utilizando a função with
with open("palavras.txt") as arquivo:
    for linha in arquivo:
        print(linha)