#pessa ao usuario para inserir um número que deseja a tabuada e em seguida exibir a tabuada do até 10
numero=int(input("Insira o número do qual deseja a tabuada: "))
i=1
x=10
for i in x:
    tabuada=numero*i
    print(numero,"x",i,"=",tabuada)
    i += 1