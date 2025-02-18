#pessa ao usuario para inserir um número que deseja a tabuada e em seguida exibir a tabuada do até 10
numero=int(input("Insira o número do qual deseja a tabuada: "))
x=[1,2,3,4,5,6,7,8,9,10]
for i in x:
    tabuada=numero*i
    print(numero,"x",i,"=",tabuada)
    i += 1