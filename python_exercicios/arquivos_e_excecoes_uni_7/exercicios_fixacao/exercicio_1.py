""" 
Exercício de fixação 1: Crie um programa que peça ao usuário uma 5 números inteiros. 
Salve estes números dentro de um arquivo chamado “números.txt”. Cada número deve ocupar uma linha.
"""

lista_numeros = []

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    lista_numeros.append(numero)

with open("números.txt", "w") as arquivo:
    for numero in lista_numeros:
        arquivo.write(str(numero) + "\n")