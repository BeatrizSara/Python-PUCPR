""" 
Laços finitos (for)
Exercício de fixação 1: Crie um programa que solicite ao usuário dez números, 
contando quantos são pares e quantos são ímpares e informando ao final essas informações.
"""
par = 0 
impar = 0

for i in range(10):
    num = int(input("Informe o " + str(i + 1) +" número: "))
    
    if num % 2 == 0:
        par += 1

    else:
        impar += 1

print("Possui {} pares".format(par))
print("Possui {} ímpares".format(impar))