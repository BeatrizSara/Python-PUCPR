""" 
Função editar_cliente()

Esta é uma função com parâmetros e com retorno. O código define uma função chamada editar_cliente 
que aceita uma lista de clientes como argumento. 
O objetivo da função é permitir que o usuário altere o nome de um cliente existente na lista.
"""

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


# Aqui está o que cada linha de código faz:

# def editar_cliente(clientes): Isto define a função editar_cliente que aceita um único argumento clientes. 
# ..A lista clientes deve conter os nomes dos clientes.

# nome_antigo = input("Insira o nome do cliente a ser editado: "): Isto solicita ao usuário que insira o ..
# ..nome do cliente que deseja editar. A entrada do usuário é então armazenada na variável nome_antigo.

# if nome_antigo in clientes: Isto verifica se o nome_antigo fornecido pelo usuário existe na lista de clientes.

# nome_novo = input("Insira o novo nome do cliente: "): Se o nome_antigo estiver na lista de clientes, então o 
# ..programa solicita ao usuário que insira o novo nome para esse cliente. O novo nome é armazenado na variável nome_novo.

# indice = clientes.index(nome_antigo) - Isto encontra o índice do nome_antigo na lista clientes. O índice é a posição 
# ...do nome_antigo na lista.

# clientes[indice] = nome_novo: Isto substitui o nome_antigo pelo nome_novo na lista de clientes.

# print(f"Cliente {nome_antigo} alterado para {nome_novo}.") - Isso informa ao usuário que o nome do cliente foi alterado com sucesso.

# else: Se o nome_antigo não estiver na lista de clientes, o programa entra nesta cláusula.

# print("Cliente não encontrado."): Isto informa ao usuário que o cliente que deseja editar não foi encontrado na lista.

# return clientes: Finalmente, a função retorna a lista atualizada de clientes.
