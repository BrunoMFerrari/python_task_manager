# Função estética para receber uma lista e imprimir ela como um menu enumerado
def menu_basico(lista_opcoes_menu, linha_superior=True, linha_inferior=True):
    index = 1
    # Imprime uma linha superior
    if linha_superior == True:
        print('='*50)

    # Cabeçalho 'MENU'
    print(f'\033[34m{'MENU':^50}\033[36m')

    # Coloca cada item de uma lista em uma linha, enumerado
    for item in lista_opcoes_menu:
        print(index,'-', item)
        index += 1

    # Imprime uma linha infeior
    if linha_inferior == True:
        print('\033[37m=\033[m'*50)


def menu_tarefas(lista_tarefas, linha_superior=True, linha_inferior=True):
    index = 1
    # Imprime uma linha superior
    if linha_superior == True:
        print('='*50)

    # Cabeçalho 
    print(f'\033[35m{'TAREFAS':^50}\033[m')

    # Imprime cada tarefa junto com seu respectivo status
    for item in lista_tarefas:

        # Adicionando prioridade nas tarefas
        if item['status'] == 'Completa':
            status = '[X]'
        elif item['status'] == 'Alta':
            status = '[Alta]'
        elif item['status'] == 'Média':
            status = '[Média]'
        elif item['status'] == 'Baixa':
            status = '[Baixa]'
        else:
            status = '[ ]'

        print(index, '-', status, item['nome'])
        index += 1

    # Imprime uma linha infeior
    if linha_inferior == True:
        print('='*50)