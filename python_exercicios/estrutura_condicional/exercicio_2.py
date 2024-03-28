""" 
Exercício de fixação 2: Crie um programa que pergunte o nome do cliente para ser inserido em um cartão de crédito, com espaço máximo de 20 caracteres. 
Caso o usuário informe um nome maior, deve mostrar uma mensagem informando que o nome é extenso demais e deve ser abreviado. 
Dica: para saber o tamanho de uma string, usar a função len. Exemplo: len(nome).
"""
nome_cliente = str(input("informe o nome para ser inserido no cartao de crédito: "))

if len(nome_cliente) > 20:
    print("O nome é extenso demais. Deve ser abreviado")
    nome_abreviado = nome_cliente[:20] # Pegara os primeiros 20 caracteres
    print(f"Nome abreviado: {nome_abreviado}")

else:
    print("Nome inserido", nome_cliente)