""" 
Exercício de fixação 7: Crie um programa que solicite ao usuário vários números e,
ao digitar 0, calcule a média dos números informados.
"""
contador = 0
total = 0

while True:
    numero = int(input("Informe um número: "))
    
    
    if numero == 0:
        break
    
    else:
        total += numero
        contador += 1
if contador > 0:
    media = total / contador
    print("A media dos números digitados foi: {}".format(media))

else:
    print("Nenhum número foi digitado")