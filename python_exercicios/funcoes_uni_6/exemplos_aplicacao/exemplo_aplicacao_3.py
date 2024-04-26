""" 
Parâmetros arbitrários
- 
Exemplo de aplicação 3: Elabore um programa que use uma função chamada somar(), 
que efetua a soma de uma quantidade aleatória de números informados, retornando 
o resultado da operação.

Uma função que possa receber um número variável de parâmetros precisa declarar um parâmetro arbitrário. 
Veja a sintaxe de função com declaração de parâmetro arbitrário:
def nomedafuncao(*args):

    print(args[0])

    print(args[1])

    ...
    
"""

def somar(*numeros):
    soma = 0
    for i in range(len(numeros)):
        soma+= numeros[i]
        
    return soma
resultado = somar(2,3,4,5,8)
print(f"A soma dos numeros é {resultado}")