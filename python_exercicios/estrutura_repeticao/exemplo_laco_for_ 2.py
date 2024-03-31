""" 
Exemplo de aplicação 2: Elabore um programa que solicite três números, 
some-os e exiba o resultado para o usuário.
"""

# Exemplo de laço for(finito)
soma = 0
for i in range(3):
    num = int(input("Digite o " + str(i + 1) + " número: "))
    soma += num
print("A soma dos números é", soma)