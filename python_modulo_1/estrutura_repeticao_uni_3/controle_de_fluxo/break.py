""" 
Exemplo comando BREAK
O comando break é usado para interromper imediatamente a execução do loop e sair dele, 
mesmo que a condição de repetição ainda seja verdadeira.
"""
for i in range(10):
    if i == 5:
        break # Interrompe o loop quando i for igual a 5
    print(i)

# Nesse exemplo, o loop será interrompido quando i for igual a 5, 
# e o programa sairá do loop.