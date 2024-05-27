""" 
Exemplo de aplicação 9: Elabore um programa que solicite um número inteiro ao usuário, 
em um intervalo entre 1 e 5.
"""
while True:
    
    try:
        num = int(input("Digite um número: "))
        if 1 <= num <=5:
            break
        else:
            print("O numero deve estar entre 1 e 5.")
    except ValueError:
        print("Valor Inválido")
print("Número validado: {}".format(num))
