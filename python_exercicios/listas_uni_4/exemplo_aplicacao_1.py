""" 
Exemplo de aplicação 1: labore um programa que solicite ao usuário cinco números, 
armazene-os em uma lista e exiba como resultado os dados obtidos.
"""
nums = [0,0,0,0,0]

for i in range(5):
    num = int(input("Digite um número: "))
    nums[i] = num
    
print(nums)

# Explicação
# Neste exemplo, criamos na linha 05 uma lista com cinco elementos zerados, 
# os quais são substituídos dentro do laço em todas as iterações da linha 09.