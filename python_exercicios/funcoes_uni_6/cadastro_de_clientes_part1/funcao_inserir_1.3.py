""" 
Função inserir_cliente()

Esta é uma função com parâmetros e com retorno. O código define uma função chamada 
inserir_cliente que recebe uma lista de clientes como argumento. 
O objetivo da função é adicionar um novo cliente a essa lista.
"""

def inserir_cliente(clientes):
    nome = input("Insira o nome do cliente: ")
    clientes.append(nome)
    
    print(f"Cliente {nome} adicionado.")

    return clientes

#Vamos dividir o código para entender melhor:

# def inserir_cliente(clientes): Isto define a função inserir_cliente que aceita um único argumento clientes. Supomos que clientes seja uma lista.
# nome = input("Insira o nome do cliente: "): Isto exibe a mensagem "Insira o nome do cliente: " para o usuário e espera que ele insira uma entrada. A entrada do usuário é então atribuída à variável nome.
# clientes.append(nome): Isto adiciona o valor da variável nome ao final da lista clientes.
# print(f"Cliente {nome} adicionado."): Isto mostra uma mensagem informando ao usuário que o cliente foi adicionado.
# return clientes: Finalmente, a função retorna a lista clientes que agora inclui o novo cliente.
