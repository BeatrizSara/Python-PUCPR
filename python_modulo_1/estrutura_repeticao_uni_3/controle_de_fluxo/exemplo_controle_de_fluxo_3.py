""" 
Exemplo de aplicação 7: Elabore um programa que solicite um número inteiro ao usuário, 
validando e imprimindo esse número.
"""
while True:
    try:
        numero = int(input("Informe um numero:"))
        break
    except ValueError:
        print("Valor Inválido")
print("Valor validado:{}".format(numero))