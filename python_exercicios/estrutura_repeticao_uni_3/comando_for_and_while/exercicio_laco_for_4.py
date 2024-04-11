""" 
Exercício de fixação 4: Crie um programa que solicite um número ao usuário e 
exiba a tabuada dele de 1 a 10, no formato:
Tabuada do n:
n x 1 = n
n x 2 = 2n
...
n x 10 = 10n
"""

numero = int(input("Qual tabuada você deseja? "))
print("Tabuada do {}".format(numero))

for i in range(1, 11):
    resultado = numero*i
    
    print("{} x {} = {}".format(numero, i, resultado))