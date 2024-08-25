# Estrutura de dados para armazenar tarefas
tarefas = {}

# Função para adicionar uma tarefa
def adicionar_tarefa(nome, descricao, prioridade, categoria):
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
def concluir_tarefa(nome):
    if nome in tarefas:
        tarefas[nome]['concluída'] = True
        print(f"Tarefa '{nome}' marcada como concluída.")
    else:
        print(f"Tarefa '{nome}' não encontrada.")

# Função para exibir tarefas por prioridade
def exibir_tarefas_por_prioridade(prioridade):
    tarefas_filtradas = {nome: detalhes for nome, detalhes in tarefas.items() if detalhes['prioridade'] == prioridade}
    if not tarefas_filtradas:
        print(f"Nenhuma tarefa encontrada com prioridade '{prioridade}'.")
    else:
        for nome, detalhes in tarefas_filtradas.items():
            print(f"Tarefa: {nome}\n  Descrição: {detalhes['descrição']}\n  Categoria: {detalhes['categoria']}\n  Status: {'Concluída' if detalhes['concluída'] else 'Pendente'}\n")

# Função para exibir tarefas por categoria
def exibir_tarefas_por_categoria(categoria):
    tarefas_filtradas = {nome: detalhes for nome, detalhes in tarefas.items() if detalhes['categoria'] == categoria}
    if not tarefas_filtradas:
        print(f"Nenhuma tarefa encontrada na categoria '{categoria}'.")
    else:
        for nome, detalhes in tarefas_filtradas.items():
            print(f"Tarefa: {nome}\n  Descrição: {detalhes['descrição']}\n  Prioridade: {detalhes['prioridade']}\n  Status: {'Concluída' if detalhes['concluída'] else 'Pendente'}\n")

# Exemplo de uso das funções
adicionar_tarefa('Estudar Python', 'Aprender sobre ambientes virtuais e pacotes', 'Alta', 'Estudo')
adicionar_tarefa('Comprar Mantimentos', 'Comprar frutas e vegetais', 'Média', 'Pessoal')
adicionar_tarefa('Exercício Físico', 'Ir à academia para malhar', 'Alta', 'Saúde')

listar_tarefas()

concluir_tarefa('Estudar Python')

exibir_tarefas_por_prioridade('Alta')
exibir_tarefas_por_categoria('Pessoal')
