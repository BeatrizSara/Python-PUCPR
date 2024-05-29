""" 
Função listar_clientes()

Esta é uma função com parâmetros e sem retorno (o return None é a mesma coisa de não informarmos nada com return). 
O código define uma função chamada listar_clientes que aceita uma lista de clientes como argumento. 
O objetivo da função é imprimir os nomes de todos os clientes presentes na lista.
"""
def listar_clientes(clientes):
    print("Lista de clientes:")

    for cliente in clientes:
        print(cliente)

    return None

# Aqui está o que cada linha de código faz:

# def listar_clientes(clientes): Isto define a função listar_clientes que aceita um único argumento clientes. ..
# ...A lista clientes deve conter os nomes dos clientes.

# print("Lista de clientes:"): Isto imprime a string "Lista de clientes:".
# for cliente in clientes: Isto inicia um loop for que percorre cada cliente na lista clientes.
# print(cliente): Para cada cliente na lista clientes, este código imprime o nome do cliente.
# return None - Finalmente, a função retorna None. Em Python, é convencional retornar None quando uma função não tem um resultado significativo para retornar. Neste caso, a função listar_clientes realiza uma ação (imprimir os nomes dos clientes), mas não tem um resultado "útil" para retornar.