""" 
Comando CONTINUE
Exemplo de aplicação 5: Elabore um programa que solicite ao usuário dez números e 
efetue a multiplicação, exibindo o resultado. 
No entanto, se em algum momento o número digitado for 0, deve pular esta iteração, 
para que o valor não seja zerado.
"""
multiplicacao = 1
for i in  range(10):
    numero = int(input("Informe o "+ str(i+1) + ("número: ")))
    if numero == 0:
        continue
    multiplicacao *= numero
print("Multiplicação dos numeros é: {}".format(multiplicacao))