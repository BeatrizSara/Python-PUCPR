""" 
Exercício de fixação 7: Crie um programa que pergunte o tamanho de três lados de um triângulo 
e informe o tipo de triângulo, a saber:
Só será um triângulo quando a soma de dois lados sempre for maior que o terceiro lado.
Equilátero: triângulo com todos os lados iguais.
Isósceles: triângulo com dois lados iguais.
Escaleno: triângulo com todos os lados diferentes.
"""
print("===== Informe três lados de um triângulo =====")

lado_1 = int(input("Primeiro lado: "))
lado_2 = int(input("Segundo lado: "))
lado_3 = int(input("Terceiro lado: "))

if lado_1 + lado_2 > lado_3 and lado_2 + lado_3 > lado_1 and lado_3 + lado_1 > lado_2:
    print("Esses valores podem formar um triângulo")
    if lado_1 == lado_2 == lado_3:
        print("Esses valores podem formar um triângulo EQUILÁTERO")
    elif lado_1 == lado_2 or lado_2 == lado_3 or lado_3 == lado_2:
        print("Esses valores podem formar um triângulo ISÓSCELES")
        
    else:
        print("Esses valores podem formar um triângulo ESCALENO")
else:
    print("Esses valores NÃO podem formar um triângulo!")
    print("Tente novamente")