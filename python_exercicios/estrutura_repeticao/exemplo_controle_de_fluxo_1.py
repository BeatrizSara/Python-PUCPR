""" 
Comando BREAK
Exemplo de aplicação 4: Elabore um programa que solicite ao usuário dez números e efetue a soma, exibindo o resultado. 
Contudo, se em algum momento o número digitado for 0, deve interromper o laço, mostrando a soma apenas dos valores informados até então.
"""

soma  = 0
for i in range(10):
    numero = int(input("Informe o "+ str(i + 1)+ " numero: "))
    if numero == 0:
        break
    soma += numero
print("Soma dos números: {} ".format(soma))