""" 
Exercício de fixação 5: Elabore um algoritmo que solicite valor de um produto e a quantidade comprada, 
informando o valor total de compra calculado.
"""

valor_produto = float(input("Informe o valor do produto: "))
quantidade_compra = int(input("Informe a quantidade do produto: "))

valor_total = valor_produto * quantidade_compra

print(f"O valor da compra foi R${valor_total:.2f}")

""" 
Entrada: 
Valor do produto
Quantidade do produto

Saída: Valor total da compra 

Passos: 
    - Peça ao usuario que informe o valor do produto
    - Guarde a resposta do usuario na variavel "valor_produto"
    - Peça ao usuario que informe a quantidade comprada
    - Guarde a resposta do usuario na variavel "quantidade_compra"
    - valor_total = valor_produto * quantidade_compra
    - Exiba a variavel "valor_total" para o usuario
"""