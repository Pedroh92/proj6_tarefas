# Estrutura de dados para armazenar tarefas
tarefas = {}

# Função para adicionar uma tarefa
def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    prioridade = input("Digite a prioridade da tarefa (Alta, Média, Baixa): ")
    categoria = input("Digite a categoria da tarefa: ")
    
    tarefas[nome] = {
        'descrição': descricao,
        'prioridade': prioridade,
        'categoria': categoria,
        'concluída': False
    }
    print(f"Tarefa '{nome}' adicionada com sucesso!")

# Função para listar todas as tarefas
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for nome, detalhes in tarefas.items():
            status = "Concluída" if detalhes['concluída'] else "Pendente"
            print(f"Tarefa: {nome}\n  Descrição: {detalhes['descrição']}\n  Prioridade: {detalhes['prioridade']}\n  Categoria: {detalhes['categoria']}\n  Status: {status}\n")

# Função para marcar uma tarefa como concluída
def concluir_tarefa():
    nome = input("Digite o nome da tarefa que deseja marcar como concluída: ")
    if nome in tarefas:
        tarefas[nome]['concluída'] = True
        print(f"Tarefa '{nome}' marcada como concluída.")
    else:
        print(f"Tarefa '{nome}' não encontrada.")

# Função para exibir tarefas por prioridade
def exibir_tarefas_por_prioridade():
    prioridade = input("Digite a prioridade das tarefas que deseja visualizar (Alta, Média, Baixa): ")
    tarefas_filtradas = {nome: detalhes for nome, detalhes in tarefas.items() if detalhes['prioridade'].lower() == prioridade.lower()}
    if not tarefas_filtradas:
        print(f"Nenhuma tarefa encontrada com prioridade '{prioridade}'.")
    else:
        for nome, detalhes in tarefas_filtradas.items():
            status = "Concluída" if detalhes['concluída'] else "Pendente"
            print(f"Tarefa: {nome}\n  Descrição: {detalhes['descrição']}\n  Categoria: {detalhes['categoria']}\n  Status: {status}\n")

# Função para exibir tarefas por categoria
def exibir_tarefas_por_categoria():
    categoria = input("Digite a categoria das tarefas que deseja visualizar: ")
    tarefas_filtradas = {nome: detalhes for nome, detalhes in tarefas.items() if detalhes['categoria'].lower() == categoria.lower()}
    if not tarefas_filtradas:
        print(f"Nenhuma tarefa encontrada na categoria '{categoria}'.")
    else:
        for nome, detalhes in tarefas_filtradas.items():
            status = "Concluída" if detalhes['concluída'] else "Pendente"
            print(f"Tarefa: {nome}\n  Descrição: {detalhes['descrição']}\n  Prioridade: {detalhes['prioridade']}\n  Status: {status}\n")

# Função para exibir o menu
def exibir_menu():
    print("\n=== Menu de Gerenciamento de Tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Listar todas as tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Exibir tarefas por prioridade")
    print("5. Exibir tarefas por categoria")
    print("6. Sair")

# Função principal para executar o programa
def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            adicionar_tarefa()
        elif escolha == '2':
            listar_tarefas()
        elif escolha == '3':
            concluir_tarefa()
        elif escolha == '4':
            exibir_tarefas_por_prioridade()
        elif escolha == '5':
            exibir_tarefas_por_categoria()
        elif escolha == '6':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()