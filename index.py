import datetime
import ast

def menu():
    print('--Menu de opções--')
    print('1. Submenu de usuários')
    print('2. Submenu de livros')
    print('3. Submenu de empréstimos')
    print('4. Submenu relatórios')
    print('5. sair')
    print()
    option = int(input('Selecione a opção:'))
    return option


def submenu(opt):
    #Cria um título para cada submenu selecionado
    if opt == 1:
        print(f'--Aba Usuários--')
    elif opt == 2:
        print('--Aba Livros--')
    elif opt == 3:
        print('--Aba Empréstimos--')
    elif opt == 4:
        print('--Aba Relatórios--')
        print()
        print('1. Listar usuários com mais de x idade')
        print('2. Listar livros com mais de x autores')
        print('3. Listar dados de empréstimos com data de devolução entre datas x e y')
        print('4. Sair da aba')
        print()
        option=int(input('Selecione a opção: '))
        print()
        return option
    #Printa as ações disponíveis para o usuário
    sair =  False
    while sair == False:
        print('1. Listar todos')
        print('2. Listar um elemento específico do conjunto')
        print('3. Incluir')
        print('4. Alterar/excluir cadastro')
        print('5. Sair da aba')
        print()
        #Recebe do usuário a opção desejada
        option =input('Selecione a opção: ')
        if option == '1' or option == '2' or option == '3' or option == '4' or option == '5':
            option = int(option)
            return option
        else:
            print()
            print('Opção inválida, selecione uma opção válida')


def calculate_age(birth_date):
    current_date = datetime.date.today()
    difference = current_date - birth_date
    age = round(difference.days / 365) #divido a diferença em dias para receber os anos e uso a função round para arredondar para um número inteiro
    return age


def get_date(option):
    while True:
        try:
            if option == 1:
                year = int(input('Ano de nascimento(aaaa): '))
                month = int(input('mês de nascimento(numeral): '))
                day = int(input('dia de nascimento: '))
                birth_date = datetime.date(year, month, day)
                return birth_date
            elif option == 3:
                year = int(input('Ano de retirada:'))
                month = int(input('Mês de retirada(numeral):'))
                day = int(input('dia de retirada: '))
                loan_date = datetime.date(year, month, day)
                return loan_date
            elif option == 4:
                year = int(input('Ano de devolução: '))
                month = int(input('Mês de devolução: '))
                day = int(input('Dia de devolução: '))
                loan_return_date = datetime.date(year, month, day)
                return loan_return_date
        except:
            print('--VALUE ERROR--')


def exist_file(name_file):
    import os
    if os.path.exists(name_file):
        return True
    else:
        return False


####################################################################################################################
############################ para criar/escrever um novo arquivo


def create_file(dict, file):
    ref_users = open(file, 'w')
    for i in dict:
        var=str(i)
        ref_users.write(var + ';') #adiciona a chave do dicionario ao primeiro item do arquivo de texto
        for j in dict[i]:
            element = str(j) #converte o elemento da lista em uma string para poder appendar
            ref_users.write(element + ';') #escreve o elemento + ;
        ref_users.write('\n') #no final adiciona uma quebra de linha ao arquivo
    ref_users.close()


#########################################################################################################
########################### para importar os dados de um arquivo ########################################


def import_data(dict, file):
    if exist_file(file):
        ref_arq = open(file, 'r') #abre o arquivo em modo leitura
        for line in ref_arq:
            list = line.split(';') #transforma os itens do arquivo em uma lista
            del list[-1] #deleta o \n da lista
            if list[0][0] == '(':
                list[0] = ast.literal_eval(list[0]) #Transforma a string de indice 0 em uma tupla
            dict[list[0]] = [] #adiciona o primeiro item da lista(cpf) como a chave do dicionario
            for i in range(1, len(list)): #começa a contagem á partir do segundo item pois o primeiro é a chave do dicionario
                if list[i][0] != '[':
                    dict[list[0]].append(list[i])
                elif list[i][0] == '[':
                        lista = ast.literal_eval(list[i])
                        dict[list[0]].append(lista) #adiciona a lista dentro da lista
    else:
        return False


####################################################################################################################################
############################## inclui um novo elemento #############################################################################


def include(dict, option):
    if option == 1:
        cpf = input('CPF: ')
        if cpf in dict:
            return False
        else:
            dict[cpf] = [] #atribui o cpf como chave do usuário
            name = input('Nome: ')
            dict[cpf].append(name) #atribui o nome ao índice 0 da lista
            street = input('Endereço(rua): ')
            dict[cpf].append(street) #atribui a rua ao índice 1 da lista
            n = input('Número(casa): ')
            dict[cpf].append(n) #atriui o numero da casa ao índice 2 da lista
            cep = input('CEP: ')
            dict[cpf].append(cep) #atribui o cep ao índice 3 da lista
            dict[cpf].append([]) #atribui a lista de email ao índice 4 da lista
            sair =  False
            while sair == False:
                mail = input('E-mail(pressione "5" para parar de adicionar emails): ')
                if mail != '5':
                    dict[cpf][4].append(mail) #adiciona o email à lista de emails
                else: 
                    sair = True
            dict[cpf].append([]) # atribui o telefone ao índice 5 da lista
            sair = False
            while sair == False:
                phone = input('Telefone(pressione "s" para parar de adicionar telefones): ')
                if phone != 's':
                    dict[cpf][5].append(phone)
                else:
                    sair = True 
            birth_date = get_date(option)
            dict[cpf].append(birth_date) #atribui a data de nasc. ao índice 6 da lista
            age = calculate_age(birth_date)
            dict[cpf].append(age) #atribui a idade ao índice 7 da lista
            prof = input('Profissão/Ocupação: ')
            dict[cpf].append(prof) # atribui a profissão ao índice 8 da lista
            create_file(dict, 'users.txt')
            return True
        
    elif option == 2:
        isbn = input('ISBN: ')
        if isbn in dict:
            return False
        else:
            dict[isbn] = []
            title = input('Título: ')
            dict[isbn].append(title) #atribui o título ao índice 0
            gender = input('Gênero: ')
            dict[isbn].append(gender) #atribui o gênero ao índice 1
            dict[isbn].append([]) #atribui uma lista para autores ao índice 2
            sair = False
            while sair == False: 
                author = input('Nome do autor (para parar de inserir autor, insira "s"): ')
                if author != 's':
                    dict[isbn][2].append(author) #adiciona os autores à lista do índice 2
                else:
                    sair = True # se o valor para a avriável for == s sai do laço de repetição
            pages_number = int(input('Número de páginas: '))
            dict[isbn].append(pages_number)
            create_file(dict, 'books.txt')
            return True

def include_loan_out(dict1, dict2, dict3):
    cpf = input('CPF do usuário que fará o empréstimo: ')
    if cpf not in dict1:
        print('--CPF não cadastrado--')
        return False
    isbn = input('ISBN do livro emprestado: ')
    if isbn not in dict2:
        print('--ISBN não cadastrado--')
        return False
    print('--data de retirada--')
    data_retirada = get_date(3)
    data_retirada = data_retirada.strftime("%Y-%m-%d") #converte a data datetime para string
    tupla = (cpf,isbn,data_retirada) #CPF = [0] - ISBN [1] - data de retirada = [3]
    if tupla in dict3: 
        print('-- ERRO EMPRÉSTIMO JÁ CADASTRADO--')
        return False
    else:
        if dict3 == {}:
            dict3[tupla] = []
            loan_return(dict3, tupla)
            create_file(dict3, 'emprestimos.txt')
            return True
        else:
            for key in dict3: #caso o usuário e o livro já estejam em algum outro empréstimo,verifica as chaves para ver se a data é válida
                if tupla[0] == key[0] and tupla[1] ==  key[1]:
                    if verify_loan_date(dict3, tupla, key): # caso a data de novo empréstimo não esteja entre a data de empréstimo e devolução do mesmo livro e usuário de outro empréstimo, cria um novo empréstimo
                        dict3[tupla] = []
                        loan_return(dict3, tupla)
                        create_file(dict3, 'emprestimos.txt')
                        return True
                    else: # se caso a data for inválida, a função retornou falso e agora exibimos a mensagem de data inválida
                        print('--ERRO DATA PARA CADASTRO INVÁLIDA--')
                        return False
                elif tupla[1] == key[1]:
                    if verify_loan_date(dict3, tupla, key):
                        dict3[tupla] = []
                        if loan_return(dict3, tupla):
                            create_file(dict3, 'emprestimos.txt')
                            return True
                        else:
                            return False
                    else:
                        print('--ERRO ESTE LIVRO ESTÁ EMPRESTADO--')
                        return False
            #caso nenhuma das proposições anteriores seja verdadeira para nenhuma chave, adiciona direto o arquivo
            dict3[tupla] = []
            loan_return(dict3, tupla)
            create_file(dict3, 'emprestimos.txt')
            return True
                

def verify_loan_date(dict, new_loan, loan): #new_loan = dados do novo empréstimo e loan = dados do empréstimo já existente
    from datetime import datetime
    data_retirada1 = new_loan[2] #recebe data de retirada do empréstimo que está sendo registrado
    data_retirada1 = datetime.strptime(data_retirada1, '%Y-%m-%d') #converte para datetime
    data_retirada2 = loan[2] #recebe a data de retirada do empréstimo já existente com o mesmo parâmetro
    data_retirada2 = datetime.strptime(data_retirada2, '%Y-%m-%d') #converte para datetime
    data_devolucao2 = dict[loan][0] #recebe a data de devolução do empréstimo já existente
    data_devolucao2 = datetime.strptime(data_devolucao2, '%Y-%m-%d') #converte para datetime
    if data_retirada2 <= data_retirada1 <= data_devolucao2: #verifica se o livro que está sendo emprestado está disponível
        return False
    else:
        return True


def loan_return(dict, key): #cadastrar os valores do empréstimo
    from datetime import datetime
    print()
    data_de_devolução = get_date(4)
    data_retirada = datetime.strptime(key[2], '%Y-%m-%d').date()
    if data_de_devolução < data_retirada:
        print('--DATA INVÁLIDA--')
        del dict[key]
    else:
        data_de_devolução = data_de_devolução.strftime('%Y-%m-%d')
        dict[key].append(data_de_devolução)
        penalty_value = float(input('Valor diário da multa por atraso: '))
        dict[key].append(penalty_value)


#######################################################################################
################ Lista todos os elementos #############################################


def list_elements(dict, op):
    #percorrendo todas as chaves do dicionário
    if op == 1:
        print('--Lista de usuários--')
    elif op == 2:
        print('--Lista de livros--')
    elif op == 3:
        print('--Lista de Empréstimos---')
        print()
        n=1
        for key in dict:
            print(f'* {n}. CPF: {key[0]}, ISBN: {key[1]}, data de retirada: {key[2]}:\n-Devolução: {dict[key][0]}\n-Valor da multa por dia de atraso: {dict[key][1]}')
            n+=1
            print()
        return True
    n = 0
    for key in dict.keys():
        #printando o índice 0 da lista(que representa o nome) de cada chave
        print(f'{n}. {dict[key][0]}({key})')
        n += 1


########################################################################################
################ Lista os dados de um elemento de acordo com a chave ###################


def list_element(dict, key):
    #percorrer cada elemento da lista da chave do dicionário
    list = 4, 5
    i = 0
    if key in dict:
        while i <= 8:
            if i == 0:
                print(f'Nome: {dict[key][i]}')
            elif i == 1:
                print(f'Rua: {dict[key][i]}')
            elif i == 2:
                print(f'Número(casa): {dict[key][i]}')
            elif i == 3:
                print(f'CEP: {dict[key][i]}')
            elif i == 4:
                index = 0
                print('Emails:')
                for index in range(len(dict[key][i])):
                    print(f'- {dict[key][i][index]}')
            elif i == 5:
                index = 0
                print('Telefones:')
                for index in range(len(dict[key][i])):
                    print(f'- {dict[key][i][index]}')
            elif i == 6:
                print(f'data de nascimento: {dict[key][i]}')
            elif i == 7:
                print(f'Idade: {dict[key][i]}')
            elif i == 8:
                print(f'Profissão: {dict[key][i]}')
            i += 1
        return True
    else:
        return False
    

    #####################################################################################################################################
##################################### Lista um livro  ##############################################################################


def list_element_livros(dict,key):
    #percorrer cada elemento da lista da chave do dicionário
    i=0
    if key in dict:
        while i<=3:
            if i == 0:
                print(f'Titulo: {dict[key][i]}')
            elif i == 1:
                print(f'Gênero: {dict[key][i]}')
            elif i == 2:
                print(f'Autor(es): ')
                for author in dict[key][i]:
                    print(f'-{author}')
            elif i == 3:
                print(f'Número de páginas: {dict[key][i]}')
            i+=1
        return True
    else:
        return False


#############################################################################################
######################### Exibe as opções de alteração ######################################


def change_options(option):
    if option == 1:
        valid = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
        sair =  False
        while sair == False:
            print('--Alterar cadastro--')
            print('0. Para alterar o nome ')
            print('1. Para alterar a rua do endereço')
            print('2. Para alterar o número da casa')
            print('3. Para alterar o CEP')
            print('4. para alterar ou adicionar email')
            print('5. Para alterar ou adicionar telefone')
            print('6. Para alterar a data de nascimento')
            print('7. para alterar a profissão') #por fins estéticos mantém o numero 7, porém o indice da profissão é 8
            print('9. para sair da aba')
            op = input('Qual opção deseja alterar: ')
            if op in valid and op != 7:
                op = int(op)
                return op
            elif op in valid and op == 7:
                op = int(op) #corrige o índice da seleção de profissão para 8
                op += 1
                return op
            else:
                print()
                print('Opção inválida')
    elif option == 2:
        valid = '0', '1', '2', '3', '9'
        sair = False
        while sair == False:
            print('--Alterar cadastro--')
            print('0. Para alterar o título')
            print('1. Para alterar o gênero')
            print('2. Para alterar o Autor')
            print('3. Para alterar o número de páginas')
            print('9. para sair da aba')
            op = input('Qual opção deseja alterar: ')
            if op in valid:
                op = int(op)
                return op
            else:
                print()
                print('Opção inválida')
    elif option == 3:
        valid = '0', '1', '2'
        sair = False
        while sair == False:
            print('--Alterar cadastro--')
            print('0. Para alterar a data de devolução')
            print('1. Para alterar o valor diário da multa por atraso')
            op = input('Qual opção deseja alterar: ')
            if op in valid:
                op=int(op)
                return op
            else:
                print()
                print('Opção invállida')


###################################################################################################
####################### para alterar o resgistro ##################################################


def change_register(dict, key, index, op): #op = menu
    if op == 1:
        if index != 4 and index != 5:   #verifica se o valor é uma lista, ou não
            if index != 6:
                dict[key][index] = input('Novo valor: ')
            else: 
                dict[key][index] = get_date(op)
                dict[key][7] = calculate_age(dict[key][6])
        else:
            if index == 4: #caso seja uma lista, dá a opção de excluir um elemento já existnte, ou cadastrar um novo
                print()
                print('1. Excluir email já existnte')
                print('2. Adicionar email(s)')
                option = int(input('Opção:'))
                if option == 1: 
                    print()
                    cont = 0
                    for i in range(len(dict[key][4])): #Caso o valor escolhido seja uma lista, percorre-a e para mostrar as opções disponíveis para serem excluídas
                        print(f'{cont}. {dict[key][4][i]}')
                        cont += 1
                    option = int(input('Qual email deseja excluir: '))
                    del dict[key][4][option]
                elif option == 2: #caso deseje adicionar um novo elemento, entr em loop até que o número 5 seja atribuído à variável "newMail" para encerrar o programa
                    sair = False
                    while sair == False:
                        newMail = input('Insira um novo email, ou pressione 5 para encerrar a aba: ')
                        if newMail != '5':
                            dict[key][4].append(newMail)
                        else:
                            print('--Encerrando programa--')
                            sair = True     
            elif index == 5: 
                print()
                option = int(input('1.para excluir\n2.para adicionar\nOpção: '))
                cont = 0
                if option == 1:
                    for i in range(len(dict[key][index])): #percorre os elementos da lista de telefones(indice[5])
                        print(f'{cont}. {dict[key][index][i]}') #printa os elementos e os numera para que o usuário possa esolher qual deseja excluir
                        cont += 1                   
                    print('Qual telefone deseja excluir?')
                    option = int(input('Opção: '))
                    del dict[key][index][option]
                elif option == 2:
                    sair = False
                    while sair == False:
                        newNumber = input('Insira um novo telefone, ou insira "e" para sair: ')
                        if newNumber != 'e':
                            dict[key][index].append(newNumber)
                        else:
                            sair = True
                            print('--ENCERRANDO ABA--')
        create_file(dict, 'users.txt')
        #Livros
    elif op == 2:
        if index != 2 and index != 3:
            dict[key][index] = input('novo valor: ')        
        elif index == 2:
            print()
            option = int(input('1.para excluir\n2.para adicionar\nopção: '))
            sair = False
            while sair ==  False:
                if option == 1:
                    cont = 0
                    for i in range(len(dict[key][index])): #percorre os elementos da lista de generos(indice[1])
                        print(f'{cont}. {dict[key][index][i]}') #printa os elementos da lista de generos
                        cont +=1
                    option = (input('Qual autor deseja remover(para encerrar a aba insira "s"): '))
                    if option != "s":
                        option = int(option)
                        del dict[key][index][option]
                        sair = True
                    else:
                        print('--ENCERRANDO ABA--')
                        sair = True
                elif option == 2:
                    new_author = input('Qual autor deseja adicionar(para encerrar a aba insira "5"): ')
                    if new_author != '5':
                        dict[key][index].append(new_author)
                    else:
                        print('--ENCERRANDO ABA--')
                #empréstimos
        elif index == 3:
            dict[key][index] = int(input('novo valor:'))
        create_file(dict, 'books.txt')
    elif op == 3:
        if index == 0:
            data_devolucao = get_date(4)
            data_devolucao = data_devolucao.strftime('%Y-%m-%d')
            dict[key][index] = data_devolucao
        elif index == 1:
            novo_valor = input('Novo valor diário da multa por atraso: ')
            dict[key][index] = novo_valor
        create_file(dict,'emprestimos.txt')
    return True        


#################################################################################################################################
############################# Lista um empréstimo ##############################################################################

def list_element_emprestimos(dict,key):
    #precorrer cada elemento da lista de uma chave do dicionário
    i=0
    if key in dict:
        while i < 2:
            if i == 0:
                print((f'Data da devolução: {dict[key][i]}'))
            elif i == 1:
                print(f'Valor diário da multa por atraso: {dict[key][i]}')
            i += 1
        return True
    else:
        return False
    

#################################################################################################################################
############################# Para deletar um elemento(chave)  ##################################################################


def del_key(dict, key, file):
    #excluir uma chave de um dicionário
    del dict[key]
    create_file(dict, file)
    return True


##################################################################################################################################
################################### Função Relatórios ############################################################################

def relatorios(dict,option, dict2, dict3):
    from datetime import datetime
    #executa os relatórios conforme escolhas do usuário
    if option == 1:
        idade=int(input('Idade: '))
        print()
        print(f'--Listando usuários com idade igual ou acima de {idade} anos--')
        print()
        for key in dict.keys():
            idade2 = int(dict[key][7])
            if idade2 >= idade:
                i=0
                while i < 9:
                    if i == 0:
                        print(f'* Nome: {dict[key][i]}')
                    elif i == 1:
                        print(f'-Rua: {dict[key][i]}')
                    elif i == 2:
                        print(f'-Número(casa): {dict[key][i]}')
                    elif i == 3:
                        print(f'-CEP: {dict[key][i]}')
                    elif i == 4:
                        index = 0
                        print('-Emails:')
                        for index in range(len(dict[key][i])):
                            print(f'= {dict[key][i][index]}')
                    elif i == 5:
                        index = 0
                        print('-Telefones:')
                        for index in range(len(dict[key][i])):
                            print(f'= {dict[key][i][index]}')
                    elif i == 6:
                        print(f'-Data de Nascimento: {dict[key][i]}')
                    elif i == 7:
                        print(f'-Idade: {dict[key][i]}')
                    elif i == 8:
                        print(f'-Profissão: {dict[key][i]}')
                    i += 1
                print()
    elif option == 2:
        autores=int(input('Informe a quantidade de autores: '))
        print()
        print(f'--Listando livros com mais de {autores} autores--')
        print()
        for key in dict.keys():
            qtd_autores = len(dict[key][2])
            if qtd_autores >= autores:
                i = 0
                while i <= 3:
                    if i == 0:
                        print(f'* Titulo: {dict[key][i]}')
                    elif i == 1:
                        print(f'-Gênero(s): {dict[key][i]}')
                    elif i == 2:
                        print(f'-Autor: {dict[key][i]}')
                    elif i == 3:
                        print(f'-Número de páginas: {dict[key][i]}')
                    i+=1
                print()
    elif option == 3:
        print('--data de devolução x--')
        data_dev_inicial = get_date(4)
        print()
        print('--data de devolução y--')
        data_dev_final = get_date(4)
        print()
        print(f'--Listando empréstimos com datas de devolução entre {data_dev_inicial} e {data_dev_final}--')
        print()
        for key in dict.keys():
            data_dev = datetime.strptime(dict[key][0], '%Y-%m-%d').date()
            if data_dev_inicial <= data_dev <= data_dev_final:
                print(f'* CPF: {key[0]}')
                print(f'-Nome do usuário: {dict3[key[0]][0]}')
                print(f'-ISBN: {key[1]}')
                print(f'-Livro do empréstimo: {dict2[key[1]][0]}')
                print(f'-Data de retirada: {key[2]}')
                print(f'-Data de devolução: {dict[key][0]}')
                print(f'-multa por dia de atraso: {dict[key][1]}')
            print()

##################################################################################################################################
################################### Função Principal #############################################################################

def main():
    op = 1
    users = {}
    import_data(users, 'users.txt')
    books = {}
    import_data(books, 'books.txt')
    emprestimos={}
    import_data(emprestimos,'emprestimos.txt')
    encerrar = False
    while encerrar == False:
        print()
        op = menu()
        #se a opção escolhida pelo usuário for 1, irá para a aba de usuários
        if op == 1:
            print()#dar um espaço para ficar mais estético
            #Estabelece uma condição para a aba users continuar sendo exibida, quando o usuário escolher 5, ele sairá da aba
            op_users = 1
            sair_usuarios =  False
            while sair_usuarios ==  False:
                op_users = submenu(op) #exibe as ações possíveis e retorna o valor para a variável op_users
                #listar todos os usuários
                if op_users == 1:
                    print()
                    list_elements(users, 1)
                    print()

                #lista um elemento e todas as suas informações à partir do CPF
                elif op_users == 2: 
                    print()
                    cpf = input('CPF do usuário: ')
                    if list_element(users, cpf):
                        print()
                    else:
                        print('--Usuário não encontrado! Deseja efetuar o cadastro?--')
                
                #incluir usuário
                elif op_users == 3:
                    print()
                    if include(users, op): #Caso o cpf ainda não esteja cadastrado, executa a função
                        print()
                        print('Usuário cadastrado com sucesso!')
                    else: #caso já exista um cpf igual cadastrado retorna falso e não efetua o cadastro
                        print()
                        print('**ERRO**\nUsuário já cadastrado!')
                
                #alterar/excluir cadastro
                elif op_users == 4:
                    print()
                    cpf = input('CPF do usuário:') #Insere o cpf do usuário para localizá-lo no dicionario e ter acesso aos dados
                    if cpf not in users:
                        print('__ERRO CADASTRO NÃO ENCONTRADO__')#exibe a mensagem caso o cpf não esteja no dicionário
                    else:
                        print('1. Para alterar cadastro\n2. Para excluir')#exibe a opção de excluir ou somente alterar o cadastro
                        option = int(input('Opção: '))#recebe a opção do usuário
                        print()
                        if option == 1:
                            sair = False
                            while sair == False:
                                change = change_options(op) #exibe as opções de alterações e retorna a escolhida para o usuário jogando dentro da variável option
                                if change != 9: #repete o menu de mudança enquanto a opção de sair não é selecionada
                                    change_register(users, cpf, change, op)
                                    print() 
                                else: # assim que for repetida exibe a mensagem de que o cadastro foi alterado
                                    print('--Cadastro alterado com sucesso!--')
                                    print()
                                    sair = True
                        elif option == 2:
                            if del_key(users, cpf, 'users.txt'): #exclui um usuário do cadastro
                                print('--Usuário excuído com sucesso!--')
                            else:
                                print('--ERRO, USUÁRIO NÃO ENCONTRADO--')
                    print()
                #Sai da aba usuários        
                elif op_users == 5:
                    print('--SAINDO DA ABA USUÁRIOS--')
                    sair_usuarios = True

        elif op == 2:
            op_livros = 0
            sair_livros =  False
            while sair_livros == False:
                print()
                #Recebe do usuário qual a ação ele quer
                op_livros = submenu(op)
                if op_livros == 1:
                    #lista todos os livros
                    print()
                    list_elements(books, op)

                elif op_livros == 2:
                    #lista um elemento e todas a´exs suas informações à partir do isbn
                    print()
                    isbn=input('ISBN do livro: ')
                    if list_element_livros(books,isbn):
                        print()
                    else:
                        print('--ISBN não encontrado! Deseja efetuar o cadastro?--')

                elif op_livros == 3:
                    #inclui um novo livro 
                    if include(books, 2):
                        print()
                        print('Livro cadastrado com sucesso!')
                        print()
                    else:
                        print()
                        print('**ERRO**\nLivro já cadastrado!')
                        print()
                elif op_livros == 4:
                    #alterar ou excluir cadastro
                    print()
                    isbn = input('ISBN do livro: ')
                    if isbn not in books.keys():
                        print('__ERRO, CADASTRO NÃO ENCONTRADO__') #exibe a mensagem caso o isbn não esteja no dicionário
                    else:
                        print('1. Para alterar cadastro\n2. Para excluir') #exibe a opção de excluir ou somente alterar o cadastro
                        option=int(input('Opção: '))
                        print()
                        if option == 1:
                            option=change_options(op)
                            change_register(books, isbn, option, op) #op = menu
                            print('Cadastro alterado com sucesso!')
                        elif option == 2:
                            del_key(books, isbn, 'books.txt')
                            print('Cadastro excluído com sucesso!')

                elif op_livros == 5:
                    print('--SAINDO DA ABA LIVROS--')
                    sair_livros = True
        elif op == 3:
            print()
            op_emprestimos = 0
            sair_emprestimos = False
            while sair_emprestimos == False:
                op_emprestimos = submenu(op)
                #recebe do usúario a opção escolhida
                if op_emprestimos == 1:
                    print()
                    #lista todos os empréstimos
                    list_elements(emprestimos,op)
                    print()
                elif op_emprestimos == 2:
                    print()
                    cpf = input('CPF: ')
                    isbn = input('ISBN: ')
                    data_retirada = input('Data de retirada(aaaa-mm-dd): ')
                    chave = (cpf,isbn,data_retirada)
                    #lista um elemento e todas suas informações
                    if list_element_emprestimos(emprestimos, data_retirada):
                        print()
                    else:
                         print('--Empréstimo não encontrado! Deseja efetuar o cadastro?--')
                elif op_emprestimos == 3:
                    print()
                    #cadastra um novo emprestimo
                    if include_loan_out(users, books, emprestimos):
                        print('Empréstimo cadastrado com sucesso!')
                        print()
                    else:
                        print()
                elif op_emprestimos == 4:
                    #alterar ou excluir cadastro
                    print()
                    cpf = input('CPF: ') #recebe cpf
                    isbn = input('ISBN: ') #recebe o isbn
                    data_retirada = get_date(3) #recebe a data
                    data_retirada = data_retirada.strftime('%Y-%m-%d') #converte a data em str
                    chave = (cpf, isbn, data_retirada) #chave tupla
                    if chave not in emprestimos: 
                        print('__ERRO, CADASTRO NÃO ENCONTRADO__')
                    else: #se a chave estiver no dict, dá as opções
                        print('1. Para alterar cadastro\n2. Para excluir') 
                        option = int(input('Opção: '))
                        if option == 1: # se aopção for alterar alguma variável, chama as funções de alteração
                            option = change_options(op) #op = menu
                            change_register(emprestimos, chave, option, op)
                            print('Cadastro alterado com sucesso!')
                            print()
                        elif option == 2:
                            del_key(emprestimos, chave, 'emprestimos.txt')
                            print('Cadastro excluído com sucesso!')
                            print()
                elif op_emprestimos == 5:
                    print('--SAINDO DA ABA EMPRÉSTIMOS--')
                    sair_emprestimos=True
        elif op == 4:
            #imprimir relatórios de acordo com a opção do usuário
            print()
            op_relatorios=submenu(op) #op = menu
            if op_relatorios == 1:
                relatorios(users, op_relatorios, None, None)
            elif op_relatorios == 2:
                relatorios(books, op_relatorios, None, None)
            elif op_relatorios == 3:
                relatorios(emprestimos, op_relatorios, books, users)

            
        #se a opção 5 for escolhida, encerra o programa
        elif op == 5:
            print()
            print('--Encerrando Programa--')
            encerrar = True            
        else:
            print()
            print('Opção inválida, insira uma opção disponível')
main()