""" 
Retornos múltiplos (tuplas)
- dá para retornar mais de um valor em um return
Exemplo de aplicação 4: Elabore um aplicativo que faça uso de uma função que 
receba diversos valores numéricos e retorne o maior e o menor valor da lista.
"""
def maior_menor(*numeros):
    maior = - 1000000
    menor = 1000000
    for numero in numeros:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    return maior, menor

resultado = maior_menor(7,15,3,22,1,8)
print(f"O maior número é {resultado[0]} e o menor numero é {resultado[1]}")
