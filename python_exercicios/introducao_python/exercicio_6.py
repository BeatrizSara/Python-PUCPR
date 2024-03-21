""" 
Exercício de fixação 6: Dê continuidade ao exercício anterior, mas com 15% de desconto sobre o valor total.
"""

valor_produto = float(input("Informe o valor do produto: "))
quantidade_compra = int(input("Informa a quantidade do produto: "))

valor_total = (valor_produto * quantidade_compra) * 0.15

""" 
Entrada: 
Valor do produto
Quantidade da compra

Saída: Valor total da compra com desconto

Passos:
    - Peça ao usuario que informe o valor do produto
    - Gaurde a resposta do usuario em uma variavel "valor_produto"
    - Peça ao usuario que informe o valor da quantidade de compra
    - Guarde a resposta do usuario em uma variavel "quantidade_compra"
    - valor_total = (valor_produto * quantidade_compra) * 0.15
    - Exiba a variavel "valor_total" da compra que foi calculada com desconto de 15% para o usuario 
"""