""" 
Exercício de fixação 2: Crie um programa que peça ao usuário cinco números 
e informe qual é o menor e qual é o maior deles.
"""
nums = []
for i in range(5):
    num = int(input("Informe o "+ str(i+1) +" número: "))
    nums.append(num)

maior = max(nums)
menor = min(nums)

print("O maior número foi {}".format(maior))
print("O menor número foi {}".format(menor))