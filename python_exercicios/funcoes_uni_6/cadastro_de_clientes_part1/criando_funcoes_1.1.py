""" 
Criando funções

Agora, como podemos criar as funções a partir do código acima? Criaremos uma função para cada uma das 
funcionalidades abaixo - logo, criaremos cinco funções:

1. Menu com as opções (sair do algoritmo, inserir clientes, editar clientes, listar clientes e pesquisar clientes);
2. Funcionalidade para inserir clientes;
3. Funcionalidade para editar clientes;
4. Funcionalidade para listar clientes;
5. Funcionalidade para pesquisar clientes.

O código final ficará assim:
"""
def menu():
    print("\nMenu:")
    print("1. Inserir clientes")
    print("2. Editar clientes")
    print("3. Listar clientes")
    print("4. Pesquisar clientes")
    print("5. Sair")

def inserir_cliente(clientes):

    nome = input("Insira o nome do cliente: ")
    clientes.append(nome)
    print(f"Cliente {nome} adicionado.")

    return clientes

def editar_cliente(clientes):
    nome_antigo = input("Insira o nome do cliente a ser editado: ")

    if nome_antigo in clientes:

        nome_novo = input("Insira o novo nome do cliente: ")
        indice = clientes.index(nome_antigo)
        clientes[indice] = nome_novo
        
        print(f"Cliente {nome_antigo} alterado para {nome_novo}.")

    else:
        print("Cliente não encontrado.")

    return clientes

def listar_clientes(clientes):
    print("Lista de clientes:")
    
    for cliente in clientes:
        print(cliente)

    return None

def pesquisar_clientes(clientes, nome):
    if nome in clientes:
        return True

    else:
        return False
    
# O código ficou maior no número de linhas, mas veja que o while True está muito menor, e mais legível.