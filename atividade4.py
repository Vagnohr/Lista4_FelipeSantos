#escreva um programa para pedir um número e em seguida o nome. exiba o nome(uma letra de cada vez em cada linha) e repita isso para o número de vezes que ele digitou
nome=input("Insira o seu nome: ")
num=int(input("Insira número de repetições: "))
for i in range(num):
    for x in nome:
        print(x)
print("Felipe Bortoluzzi dos Santos")