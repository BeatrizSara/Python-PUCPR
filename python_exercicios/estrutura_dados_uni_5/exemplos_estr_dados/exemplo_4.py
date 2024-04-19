""" 
Exemplo de aplicação 4: Elabore um programa que solicite ao usuário o 
cadastro de endereços para entrega de produtos de uma loja.
"""
enderecos = []
print("Cadastro de Endereços de Entrega")
while True:
    logradouro = input("Digite o logradouro: ")
    numero = int(input("Digite o número: "))
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")
    novo_endereco = (logradouro, numero, bairro, cidade, estado) # Criado novo endereço uma tupla novo_endereco com os detalhes do endereço fornecidos.
    enderecos.append(novo_endereco) # Adiciona a tupla novo_endereco à lista enderecos. Agora temos uma lista com várias tuplas dentro dela?
    if input("Deseja cadastrar um novo endereço (s/n)? ") == "n":
        break
print("Os endereços cadastrados são: ")
for i in range(0, len(enderecos)):
    endereco = enderecos[i]
    print(f"{i}.{endereco[0]}, {endereco[1]}, {endereco[2]} - {endereco[3]}/{endereco[4]}")