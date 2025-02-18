#pessa ao usuario para inserir seu nome e um número. se o número for menor que 10, exiba o nome dele esse número de vezes, caso contrario exiba a mensagem "número muito alto"
nome=input("Insira o seu nome: ")
numero=int(input("Insira um número: "))
for i in range(numero):
    if numero < 10:
        print(nome)
        i+=1
    else:
        print("Número muito alto")
print("Felipe Bortoluzzi dos Santos")