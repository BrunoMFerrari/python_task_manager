# Função para ler o arquivo e colocar todas as informações em um lista
def ler_arquivo(arquivo):
    lista_tarefas = []
    tarefa = {}


    with open(arquivo, 'r', encoding='utf-8') as arquivo:
        lista_linhas = arquivo.readlines()


        # Retirando o '\n' de dentro das strings
        for linha in lista_linhas:

            # Verificando o status da tarefa primeiramente
            if '[X]' in linha:
                linha = linha.replace('[X]', '')
                tarefa['status'] = 'Completa'
            elif '[Alta]' in linha:
                linha = linha.replace('[Alta]', '')
                tarefa['status'] = 'Alta'
            elif '[Média]' in linha:
                linha = linha.replace('[Média]', '')
                tarefa['status'] = 'Média'
            elif '[Baixa]' in linha:
                linha = linha.replace('[Baixa]', '')
                tarefa['status'] = 'Baixa'
            elif '[ ]' in linha:
                linha = linha.replace('[ ]', '')
                tarefa['status'] = 'Nula'

            # Salvando o título da tarefa
            linha = linha.replace('\n', '')
            linha = linha.strip()
            tarefa['nome'] = linha

            # Adicionando cada tarefa na lista geral
            lista_tarefas.append(tarefa.copy())

    # Retornando a lista de tarefas limpa
    return lista_tarefas


# Função para receber uma lista de tarefas e adiciona-las no arquivo
def upload_arquivo(arquivo, lista_tarefas):
    with open(arquivo, 'w', encoding='utf-8') as arquivo:
        for item in lista_tarefas:

            # Prioridade das tarefas
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

            if item == lista_tarefas[-1]:
                arquivo.write(status + item['nome'])
            else: 
                arquivo.write(status + item['nome'] + '\n')

        
