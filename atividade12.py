quantidade=int(input("Insira quantos horarios deseja adicionar: "))
horarios=[]
tomado=[]
for i in range(quantidade):
    horario=input("Insira quais horarios estão disponiveis: ")
    horarios.append(horario)
print(horarios)
cliente=input("Insira qual horario deseja ocupar: ")
horarios.remove(cliente)
tomado.append(cliente)
outro=input("mais algum cliente deseja marcar hora? ")
for i in range(len(horarios)):
    if "S" in outro or "s" in outro:
        print("horarios livres:",horarios,"horarios ocupados:",tomado)
        cliente=input("Insira qual horario deseja ocupar: ")
        horarios.remove(cliente)
        tomado.append(cliente)
        outro=input("mais algum cliente deseja marcar hora? ")
    elif "N" or outro or "n" in outro:
        print("Obrigado por vir")
else:
    print("todos os horarios marcados")
print("Felipe Bortoluzzi dos Santos")