""" 
Exercício de fixação 7: Crie um programa que pergunte o tamanho de três lados de um triângulo e informe o tipo de triângulo, a saber:

Só será um triângulo quando a soma de dois lados sempre for maior que o terceiro lado.
Equilátero: triângulo com todos os lados iguais.
Isósceles: triângulo com dois lados iguais.
Escaleno: triângulo com todos os lados diferentes.
"""
soma = 0
num = -1
while True:
    num = int(input("Digite um número para somar (0 finaliza): "))
    if num == 0:
        break;
    soma += num
print("A soma dos números é ", soma)