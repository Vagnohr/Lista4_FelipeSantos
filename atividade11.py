#Você é um desenvolvedor de sistemas trabalhando em um projeto colaborativo com sua equipe. Para garantir que todas as tarefas do projeto sejam concluídas dentro do prazo, você decide criar um pequeno programa para controlar o status das tarefas. O programa deve permitir que você insira o nome de cada tarefa e indique se ela está concluída ou não. No final, o programa deve apresentar um resumo com o total de tarefas, quantas estão concluídas e quantas ainda estão pendentes. Desenvolva um programa em Python que: Solicite ao usuário o número de tarefas a serem inseridas. Para cada tarefa, solicite o nome da tarefa e se ela está concluída (aceitando "sim", "s", "não" ou "n"). Conte e exiba o número de tarefas concluídas e não concluídas.
total_tarefas=int(input("Insira quantas tarefas serão feitas: "))
tarefas_concluidas=0
tarefas_inconcluidas=0
for i in range(total_tarefas):
    nome=input("Insira o nome da tarefa: ")
    tarefa=input("Insira se a tarefa foi concluida ou não: ")
    if "S" in tarefa or "s" in tarefa:
        tarefas_concluidas=tarefas_concluidas+1
    if "N" in tarefa or "n" in tarefa:
        tarefas_inconcluidas=tarefas_inconcluidas+1
print("Total de tarefas: {}".format(total_tarefas))
print("Total de tarefas concluidas: {}".format(tarefas_concluidas))
print("Total de tarefas não concluidas: {}".format(tarefas_inconcluidas))
print("Felipe Bortoluzzi dos Santos")