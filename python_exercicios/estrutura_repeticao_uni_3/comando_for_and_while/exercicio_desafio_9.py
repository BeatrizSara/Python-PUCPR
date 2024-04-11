""" 
Desafio
Exercício de fixação 9: Crie um programa que simule um carrinho de compras, solicitando o nome do produto (não pode ser vazio), seu valor (valor decimal, positivo) 
e quantidade a ser comprada (valor inteiro, positivo). Ao incluir um produto, deve perguntar se o usuário deseja fechar o pedido ou incluir mais produtos. 
Todos os dados devem ser validados. Ao final da compra, deve ser informado o valor total do pedido.
"""
total_pedido = 0

while True:
    produto = input("Informe o nome do produto ou (digite'fim' para encerrar): ")
    
    if produto.lower() == "fim":
        break
    
    while True:
        try:
            valor = float(input("Qual o valor do produto: "))
            quantidade = int(input(f"Quanto de {produto} deseja levar: "))
            
            if valor <= 0 or quantidade <= 0:
                raise ValueError("O valor e a quantidade devem ser positivos ")
            
            total_produto = valor * quantidade
            total_pedido += total_produto
            break
        except ValueError as e: # é usado para capturar a exceção que ocorreu
            print(e)
            
    print("Valor total do pedido: R$ {:.2f}".format(total_pedido))        