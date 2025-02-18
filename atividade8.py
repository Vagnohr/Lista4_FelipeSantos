#defina uma variavel chamada total como 0. pessa ao usuario para inserir 5 números e, após cada entrada pergunte se ele deseja se esse número seja incluido(S ou s, N ou n). se ele desejar, adicione o número ao total. se ele não quiser incluilo não o adicione ao total. depois de inserir 5 números exiba o total
total =0
vezes=[1,2,3,4,5]
for i in enumerate(vezes):
    acrescentar=int(input("Insira um número: "))
    deseja=input("deseja acrescentar o número? ")
    if "S" or "s" in deseja:
        total= total+acrescentar
        i = i+1
    elif "N" or "n" in deseja:
        i= i+1