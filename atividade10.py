#Faça um programa que pergunte quantas pessoas o usuário deseja convidar para uma festa. Se ele digitar um número abaixo de 10, peça os nomes e após cada nome exiba a mensagem: "[nome] está convidado para a festa".  Se ele inserir um número 10 ou superior, exiba a mensagem "Muitas pessoas".
pessoas=int(input("Insira quantas pessoa ira convidar: "))
for i in range(pessoas):
    if pessoas<10:
        nome=("Insira o nome do conidado: ")
        print("{} está convidado convidado para a festa".format(nome))
else:
    print("Muitas pessoas")
print("Felipe Bortoluzzi dos Santos")