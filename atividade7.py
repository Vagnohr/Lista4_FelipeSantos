#pessa ao usuario para inserir seu nome e um número. se o número for menor que 10, exiba o nome dele esse número de vezes, caso contrario exiba a mensagem "número muito alto"
nome=input("Insira o seu nome: ")
numero=int(input("Insira um número: "))
i = 1
if numero < 10:
    for i in str(numero):
        print(nome)
        i +=1
else:
    print("número muito alto")