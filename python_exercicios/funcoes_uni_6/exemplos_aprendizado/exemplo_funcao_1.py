""" 
Exemplo Simples

criar uma função para calcular o quadrado de um número 
(isto é, aquele número multiplicado por ele mesmo)
"""

def quadrado(numero):
    resultado = numero ** 2
    return resultado

for i in range(21):
    print(f"{i} * {i} = {quadrado(i)}")
    
""" 
As três primeiras linhas são uma nova função chamada quadrado. 
Veja que podemos chamar esta função várias vezes - neste exemplo, 
20 vezes dentro de um for.
"""