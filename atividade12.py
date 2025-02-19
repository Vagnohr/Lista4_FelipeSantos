quantidade=int(input("Insira quantos horarios deseja adicionar: "))
horarios=[]
for i in range(quantidade):
    horario=input("Insira quais horarios estão disponiveis: ")
    horarios.append(horario)
print(horarios)
cliente=input("Insira qual horario deseja ocupar: ")
tomado=horarios.remove(cliente)
outro=input("mais algum cliente deseja marcar hora? ")
if "S" in outro or "s" in outro:
    print(horarios)
    cliente=input("Insira qual horario deseja ocupar: ")
    tomado=horarios.remove(cliente)
    outro=input("mais algum cliente deseja marcar hora? ")
elif "N" or outro or "n" in outro:
    print("Obrigado por vir")
print("Felipe Bortoluzzi dos Santos")