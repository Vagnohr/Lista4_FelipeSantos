#defina uma variavel chamada total como 0. pessa ao usuario para inserir 5 números e, após cada entrada pergunte se ele deseja se esse número seja incluido(S ou s, N ou n). se ele desejar, adicione o número ao total. se ele não quiser incluilo não o adicione ao total. depois de inserir 5 números exiba o total
total=0
vezes=5
for i in range(vezes):
    acrescentar=int(input("Insira um número: "))
    deseja=input("deseja acrescentar o número? ")
    if "S" in deseja or "s" in deseja:
        total= total+acrescentar
        i+=1
    elif "N" in deseja or "n" in deseja:
        i+=1
print(total)
print("Felipe Bortoluzzi dos Santos")