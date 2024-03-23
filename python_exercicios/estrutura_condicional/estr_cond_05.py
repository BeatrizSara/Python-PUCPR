""" 
Exemplo de aplicação 5: Elabore um programa que solicite três números diferentes ao usuário 
e informe qual deles é o menor.
"""
import time

print("Informe três numeros aleatorios a seguir")
time.sleep(1)  # Pausa por 1 segundo
numero_1 = int(input("Primeiro numero: "))
numero_2 = int(input("Segundo numero: "))
numero_3 = int(input("Terceiro numero: "))
    
if numero_1 < numero_2 and numero_1 < numero_3:
    print("O numero {} é o menor!".format(numero_1))

elif numero_2 < numero_1 and numero_2 < numero_3:
    print("O numero {} é o menor!".format(numero_2))

else:
    print("O numero {} é o menor!".format(numero_3))
