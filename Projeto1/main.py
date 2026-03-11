import def_menu
import def_database
from pathlib import Path


# Função para salvamento automatico
def salvar(arquivo_txt, lista_tarefas):
    def_database.upload_arquivo(arquivo_txt, lista_tarefas)


# Nome e caminho do arquivo txt usado
arquivo_txt = Path('database_tarefas.txt')

# Definindo opções do menu
lista_opcoes_menu = ['Adicionar tarefa', 'Remover tarefa', 'Marcar como concluída', 'Editar prioridade', 'Listar tarefas']
# Coletando tarefas que já estão no sistema
lista_tarefas = def_database.ler_arquivo(arquivo_txt)

while True:

    # Criando lista de opções do meu menu e chamando uma função para organiza-las esteticamente
    def_menu.menu_basico(lista_opcoes_menu)
    # Recebendo decisão do usuário
    input_ = int(input('\033[30mOque deseja fazer?:  \033[m'))

    # 1 - Adicionar tarefa
    if input_ == 1:
        print('='*50)
        nome_nova_tarefa = str(input('\033[30mQual é a tarefa que deseja adicionar?: \033[m'))
        status_nova_tarefa = int(input('\033[30mQual a prioridade da nova tarefa? \n1 - Alta \n2 - Média \n3 - Baixa \n4 - Sem prioridade \n--> \033[m'))
        print('='*50)

        # Verificando se a tarefa já está na lista
        presenca = False
        for item in lista_tarefas:
            if item['nome'] == nome_nova_tarefa:
                presenca = True
        
        # Caso ela não esteja a adicione
        if presenca == False:

            # Adicionando a prioridade da tarefa
            if status_nova_tarefa == 1:
                status_nova_tarefa = 'Alta'
            elif status_nova_tarefa == 2:
                status_nova_tarefa = 'Média'
            elif status_nova_tarefa == 3:
                status_nova_tarefa = 'Baixa'
            elif status_nova_tarefa == 4:
                status_nova_tarefa = 'Nula'

            nova_tarefa = {'status' : status_nova_tarefa, 'nome' : nome_nova_tarefa}
            lista_tarefas.append(nova_tarefa.copy())
            print('\033[32mNOVA TAREFA ADICIONADA COM SUCESSO!!\033[m')
        else:
            print('\033[31mEssa tarefa já está na sua lista\033[m')

        # Salavamento automático das alterações
        salvar(arquivo_txt, lista_tarefas)

    # 2 - Remover tarefa
    elif input_ == 2:
        # Mostrando as tarefas atuáis e pegando a que se deseja remover
        def_menu.menu_tarefas(lista_tarefas)
        tarefa_del = str(input('\033[30mQual tarefa você deseja deletar da sua lista? \nDigite o nome ou o index dela. \n--> \033[m'))
        print('='*50)
        index = 0

        # Eliminando a tarefa desejada caso usuário tenha digitado o INDEX dela
        try:
            index = int(tarefa_del)
            lista_tarefas.pop(index-1)
            print('TAREFA REMOVIDA COM SUCESSO!!')

        # Eliminando a tarefa desejada caso usuário tenha digitado o NOME dela
        except ValueError:
            for item in lista_tarefas:
                if item['nome'] == tarefa_del:
                    lista_tarefas.pop(index)
                index += 1 
            print('\033[32mTAREFA REMOVIDA COM SUCESSO!!\033[m')

        # Salavamento automático das alterações
        salvar(arquivo_txt, lista_tarefas)

    # 3 - Marcar como concluída
    elif input_ == 3:
        # Mostrando as tarefas atuáis e pegando a que se deseja marcar como concluída
        def_menu.menu_tarefas(lista_tarefas)
        tarefa_finish = str(input('\033[30mQual tarefa você deseja concluir? \nDigite o nome ou o index dela. \n--> \033[m'))
        print('='*50)
        index = 0

        # Concluindo a tarefa desejada caso usuário tenha digitado o INDEX dela
        try:
            index = int(tarefa_finish)

            # Caso a tarefa já estava concluída
            if lista_tarefas[index-1]['status'] == 'Completa':
                # Dando opção de remover tarefa já completa
                del_ = str(input('\033[31mEssa tarefa já foi concluída, deseja remove-la da lista? (S/N): \033[m'))
                print('='*50)
                if del_ == 'S' or del_ == 's':
                    print('\033[32mTAREFA REMOVIDA COM SUCESSO!!\033[m')
                    lista_tarefas.pop(index-1)
    
            # Concluindo a tarefa
            else: 
                print('\033[32mTAREFA COMPLETA, PARABÉNS!!\033[m')
                lista_tarefas[index-1]['status'] = 'Completa'


        # Concluindo a tarefa desejada caso usuário tenha digitado o NOME dela
        except ValueError:
            # Localizando tarefa desejada
            presenca = False
            for item in lista_tarefas:
                if item['nome'] == tarefa_finish:
                    presenca = True

                    # Caso a tarefa já estava concluída
                    if item['status'] == 'Completa':
                        # Dando opção de remover tarefa já completa
                        del_ = str(input('\033[31mEssa tarefa já foi concluída, deseja remove-la da lista? (S/N): \033[m'))
                        if del_ == 'S' or del_ == 's':
                            print('\033[32mTAREFA REMOVIDA COM SUCESSO!!\033[m')
                            lista_tarefas.pop(index)
                    
                    # Concluindo a tarefa
                    else:
                        print('\033[32mTAREFA COMPLETA, PARABÉNS!!\033[m')
                        item['status'] = 'Completa'

                        
            if presenca == False:
                print('\033[31mA tarefa digitada não está na lista\033[m')

                index += 1
        
        # Salavamento automático das alterações
        salvar(arquivo_txt, lista_tarefas)

    # 4 - Editar prioridade da tarefa
    elif input_ == 4:
        def_menu.menu_tarefas(lista_tarefas)
        tarefa_edit = str(input('\033[30mQual tarefa você deseja editar a prioridade? \nDigite o nome ou o index dela. \n--> \033[m'))
        print('='*50)
        index = 0

        try:
            index = int(tarefa_edit)

            if lista_tarefas[index-1]['status'] == 'Completa':
                print('\033[31mEssa tarefa já está completa, não é possível mudar sua prioridade\033[m')
            else:
                nova_prioridade = int(input(f'\033[30mQual é a prioridade da tarefa: {lista_tarefas[index-1]['nome']} \n1 - Alta \n2 - Média \n3 - Baixa \n4 - Sem prioridade \n--> \033[m'))
                if nova_prioridade == 1:
                    status = 'Alta'
                elif nova_prioridade == 2:
                    status = 'Média'
                elif nova_prioridade == 3:
                    status = 'Baixa'
                else:
                    status = 'Nula'
                lista_tarefas[index-1]['status'] = status
                print('='*50)
                print('\033[32mPRIORIDADE ATUALIZADA COM SUCESSO!!\033[m')

        except ValueError:
            # Localizando tarefa desejada
            presenca = False
            for item in lista_tarefas:
                if item['nome'] == tarefa_edit:
                    presenca = True

                    # Caso a tarefa já estava concluída
                    if item['status'] == 'Completa':
                        # Dando opção de remover tarefa já completa
                        del_ = str(input('\033[31mEssa tarefa já foi concluída, deseja remove-la da lista? (S/N): \033[m'))
                        if del_ == 'S' or del_ == 's':
                            print('\033[32mTAREFA REMOVIDA COM SUCESSO!!\033[m')
                            lista_tarefas.pop(index)
                    
                    # Alterando prioridade da tarefa
                    else:
                        nova_prioridade = int(input(f'\033[30mQual é a prioridade da tarefa: {lista_tarefas[index]['nome']} \n1 - Alta \n2 - Média \n3 - Baixa \n4 - Sem prioridade \n--> \033[m'))
                        print('='*50)
                        if nova_prioridade == 1:
                            status = 'Alta'
                        elif nova_prioridade == 2:
                            status = 'Média'
                        elif nova_prioridade == 3:
                            status = 'Baixa'
                        else:
                            status = 'Nula'
                        print('\033[32mPRIORIDADE ATUALIZADA COM SUCESSO!!\033[m')
                        item['status'] = status
                index += 1

                        
            if presenca == False:
                print('\033[31mA tarefa digitada não está na lista\033[m')

        # Salavamento automático das alterações
        salvar(arquivo_txt, lista_tarefas)

    # 5 - Listar tarefas
    elif input_ == 5:
        # Menu lista com cabeçalho 'Tarefas:', com linhas superiores e sem as inferiores
        def_menu.menu_tarefas(lista_tarefas, True, False)
