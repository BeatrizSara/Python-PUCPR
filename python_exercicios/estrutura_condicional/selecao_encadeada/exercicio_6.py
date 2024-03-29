""" 
Seleção Encadeada
Exercício de fixação 6: Crie um programa que solicite ao usuário dois números e a operação que deseja executar entre eles. 
Mostre o resultado dessa operação no formato: num1 op num2 = resultado.
"""
num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
operacao = str(input("Qual operação deseja executar entre eles: (+), (-), (*) ou (/): "))
resultado = 0
invalido = False

if operacao == "+":
    resultado = num_1 + num_2
    
elif operacao == "-":
    resultado = num_1 - num_2

elif operacao == "*":
    resultado = num_1 * num_2

elif operacao == "/":
    resultado = num_1 / num_2
else:
    invalido = True

if invalido:
    print("Valor Inválido")
else:
    print(num_1, operacao, num_2,"=", resultado)