#pessa um número abaixo de 50 e em seguida fassa um contagem regressiva até esse número, certificando-se desmotrar o número que eles inseriram na saida
num=int(input("Insira um número abaixo de 50: "))
if num<50:
    for i in range(num,51):
        print(i)
        print(num)
else:
    print("Número invalido")