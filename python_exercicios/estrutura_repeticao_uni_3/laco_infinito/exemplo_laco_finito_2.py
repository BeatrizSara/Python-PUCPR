""" 
Exemplo de aplicação 2: Elabore um programa que solicite três números, 
some-os e exiba o resultado para o usuário.
"""
soma = 0
for i in range(3):
    numero = int(input("Informe o " + str(i +1) + " número: "))
    soma += numero # soma = soma + numero
    
print("A soma dos numeros foi {}".format(soma))