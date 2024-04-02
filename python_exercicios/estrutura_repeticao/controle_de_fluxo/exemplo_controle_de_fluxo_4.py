""" 
Exemplo de aplicação 8: Elabore um programa que solicite um número decimal ao usuário, 
validando e imprimindo esse número.
"""
while True:
    try:
        num = float(input("Digite um número: "))
        break
    except ValueError:
        print("Valor Inválido")

print("Numero validado: {}".format(num))