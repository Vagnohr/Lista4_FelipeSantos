#pessa ao usuario para inserir seu nome e um número. se o número for menor que 10, exiba o nome dele esse número de vezes, caso contrario exiba a mensagem "número muito alto"
nome=input("Insira o seu nome: ")
numero=int(input("Insira um número: "))
numeros=[1,2,3,4,5,6,7,8,9,10]
vezes = numeros.pop(numero)
for i,numero in numeros:
    if numero >= vezes:
        print(nome)
        i+=1
    else:
        print("Número muito alto")