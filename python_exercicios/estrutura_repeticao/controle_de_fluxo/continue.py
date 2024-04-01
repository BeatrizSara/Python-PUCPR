""" 
Exemplo Comando CONTINUE
O comando continue é usado para pular a iteração atual do loop e continuar com a próxima iteração, 
sem executar o restante do código dentro do loop na iteração atual.
"""

for i in range(10):
    if 1 % 2 == 0:
        continue # pula números pares
    print(i)
    
# Nesse exemplo, o continue faz com que o loop pule os números pares 
# e continue com a próxima iteração.