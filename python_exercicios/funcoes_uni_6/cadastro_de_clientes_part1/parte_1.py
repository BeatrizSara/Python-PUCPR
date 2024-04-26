""" 
Cadastro de Clientes, Parte I
O trabalho da nossa disciplina trata de um sistema de gestão de uma Universidade, e isto inclui operações como mostrar um menu e ter funcionalidades como criar cadastros, listar e remover. O objetivo desta seção é o de demostrar para você um outro caso de uso parecido: um sistema para cadastro de clientes. Quem sabe você não consegue pegar algumas ideias e inspirações a partir deste nosso exemplo?

O nosso código terá as seguintes funcionalidades:

1. Menu com as opções (sair do algoritmo, inserir clientes, editar clientes, listar clientes e pesquisar clientes);
2. Funcionalidade para inserir clientes;
3. Funcionalidade para editar clientes;
4. Funcionalidade para listar clientes;
5. Funcionalidade para pesquisar clientes.

Uma proposta para o uso
Considere o estudo que fizemos. Temos de imaginar, dentro do escopo do uso de nosso código, 
como melhor dividir nosso projeto. Verifique a proposta de código abaixo. Como é uma proposta, 
existem diferentes formas de implementarmos um código que alcance os mesmos objetivos. Logo, 
saiba que não estamos restritos a somente usar as técnicas apresentadas aqui.

Dito isso, veja e teste esta implementação. Veja que ela não possui funções em nenhum lugar:

"""
clientes = []


while True:
    print("\nMenu:")
    print("1. Inserir clientes")
    print("2. Editar clientes")
    print("3. Listar clientes")
    print("4. Pesquisar clientes")
    print("5. Sair")

    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        nome = input("Insira o nome do cliente: ")
        clientes.append(nome)
        print(f"Cliente {nome} adicionado.")

    elif opcao == 2:
        nome_antigo = input("Insira o nome do cliente a ser editado: ")
        if nome_antigo in clientes:
            nome_novo = input("Insira o novo nome do cliente: ")
            indice = clientes.index(nome_antigo)
            clientes[indice] = nome_novo
            print(f"Cliente {nome_antigo} alterado para {nome_novo}.")

        else:
            print("Cliente não encontrado.")

    elif opcao == 3:
        print("Lista de clientes:")
        for cliente in clientes:
            print(cliente)

    elif opcao == 4:
        nome = input("Insira o nome do cliente a ser pesquisado: ")

        if nome in clientes:
            print(f"Cliente {nome} está na lista.")

        else:
            print("Cliente não encontrado.")

    elif opcao == 5:
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")