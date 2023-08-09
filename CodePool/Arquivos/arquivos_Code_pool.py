#para abrir um arquivo

# arquivo = open("palavras.txt", "w")
# arquivo.write("banana")
# arquivo.write("melancia")
# arquivo.close()

arquivo = open("palavras.txt", "a")
arquivo.write("morango\n")
arquivo.write("maça\n")
arquivo.close()

# Para abrir uma imagem devemos usar:
imagem = open("foto.jpg", "rb")

#o código abaixo cria uma cópia de uma imagem:
#arquivo copia.py
logo = open('python-logo.png', 'rb')
data = logo.read()
logo.close()

logo2 = open('python-logo2.png', 'wb')
logo2.write(data)
logo2.close()