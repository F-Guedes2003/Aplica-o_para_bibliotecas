def menu():
    print('1.To add contact')
    print('2.To add a number')
    print('3.To change the contact')
    option = int(input('Qual opção deseja: '))
    return option

########################################
######### create contact ################

def create_contact(dict, key):
    dict[key] = []
    qtd = int(input('how many numbers did you want to add: '))
    for i in range(qtd):
        number = input('input a new number: ')
        dict[key].append(number)
    save_contact(dict, key)

##########################################
######### gravar contato #################

def save_contact(dict, key):
    ref_contatos = open('contatos.txt', 'w')
    line = ''
    for key in dict.keys():
        line += key + ';'
        for i in range(len(dict[key])):
            line += dict[key][i] + ';'
        line += '\n'
    ref_contatos.write(line)
    ref_contatos.close()

###########################################
######## salvar no dicionario #############

def import_contacts(arquivo):
    if arquivo_existe(arquivo):
        arq = open(arquivo, 'r')
        lista = {}
        for i in arq:
            line = i.split(';')
            lista[line[0]] = []
            for i in range(1, len(line)):
                    lista[line[0]].append(line[i])
                    if lista[line[0]][i-1] == '\n':
                        del lista[line[0]][i-1]
    print(line)
    print(lista)


###########################################
##### verificar se o arquivo existe ####### 

def arquivo_existe(nome_arquivo):
    import os
    if os.path.exists(nome_arquivo):
        return True
    else:
        return False

def main():
    agenda = {}
    op = 0
    while op != 5:
        op = menu()
        if op == 1:
            name = input('Contact name: ')
            create_contact(agenda, name)
        elif op ==  2:
            import_contacts('contatos.txt')

main()