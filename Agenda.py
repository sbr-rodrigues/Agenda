
# Programa de Gerenciamento de Tarefas

# Lista para armazenar as tarefas
tarefas = []

# Função para adicionar uma tarefa
def adicionar_tarefa(tarefa):
    tarefas.append({"tarefa": tarefa, "concluida": False})
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

# Função para visualizar todas as tarefas
def visualizar_tarefas():
    if tarefas:
        print("Suas tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{i}. {tarefa['tarefa']} - {status}")
    else:
        print("Nenhuma tarefa encontrada.")

# Função para marcar uma tarefa como concluída
def marcar_concluida(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        print(f"Tarefa '{tarefas[indice]['tarefa']}' marcada como concluída!")
    else:
        print("Índice inválido.")

# Função para remover uma tarefa
def remover_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefa_removida = tarefas.pop(indice)
        print(f"Tarefa '{tarefa_removida['tarefa']}' removida com sucesso!")
    else:
        print("Índice inválido.")

# Menu do programa
def menu():
    while True:
        print("\nMenu de Gerenciamento de Tarefas")
        print("1. Adicionar uma tarefa")
        print("2. Visualizar todas as tarefas")
        print("3. Marcar uma tarefa como concluída")
        print("4. Remover uma tarefa")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            tarefa = input("Digite a tarefa: ")
            adicionar_tarefa(tarefa)
        elif escolha == '2':
            visualizar_tarefas()
        elif escolha == '3':
            indice = int(input("Digite o índice da tarefa a ser marcada como concluída: ")) - 1
            marcar_concluida(indice)
        elif escolha == '4':
            indice = int(input("Digite o índice da tarefa a ser removida: ")) - 1
            remover_tarefa(indice)
        elif escolha == '5':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()