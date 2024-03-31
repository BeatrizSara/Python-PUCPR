""" 
Desenvolva um algoritmo que peça um número inteiro para o usuário. 
Em seguida, o algoritmo deve mostrar os dez números seguintes que vem logo após ele
"""
numero = int(input("Informe um numero: "))
for c in range(1, 11):
    print(numero + c)