""" 
Seleção Simples
Exemplo de aplicação 1: Crie um algoritmo que peça para que o usuário digite um número.
Se o número for par, então mostre na tela uma mensagem chamada “Este número é par”.
"""

numero = int(input("Informe um numero: "))

if numero %2 == 0 :
    print(f"O numero {numero} é par")
    
""" 
Entrada: Numero digitado pelo usuario

Saida: Mensagem do numero se é par ou caso contrario nao sera exibido nenhuma mensagem

Passos:
    - Peça ao usuario para informa um numero
    - Guarde esse resposta na variavel "numero"
    - Se o numero %2 igual a 0, entao:
        - Mostre a mensagem "O numero é par".
"""