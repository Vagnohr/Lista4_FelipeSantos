#fassa um programa que pergunte em qual direção o usuario deseja contar(C/c, A/a) se ele selecionar para cima, pessa um numero superior, e conte de 1 até esse número. se ele selecionar para baixo pessa a ele para inserir um número abaixo de 20 e em seguida faça contagem regressiva de 20 até esse número, se ele inserir algum valor que seja diferente, exiba a mensagem "diressão invalida"
direcao=input("Insira qual direção deseja ir: ")
if "C" in direcao or "c" in direcao:
    num=int(input("Insira um número:"))
    for i in range(num):
        print(i+1)
    print("Felipe Bortoluzzi dos Santos")
elif "A" in direcao or "a" in direcao:
    num=int(input("insira um número abaixo de 20: "))
    for i in range(num,21)[::-1]:
        print(i)
    print("Felipe Bortoluzzi dos Santos")