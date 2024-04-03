""" 
Seleção Composta
Exercício de fixação 4: Crie um programa que solicite ao usuário o seu salário. Se o valor for inferior a R$ 5.000, calcule um abono de fim de ano de 15%. 
Caso contrário, o abono será de 10%. Informe ao usuário seu valor de abono de fim de ano.
"""
# Solicita o salário do usuário
salario = float(input("Qual o seu salario: "))

# Verifica o valor do abono com base no salario
if salario < 5000:
    abono = salario * 0.15
else:
    abono = salario * 0.1

# Exibe o valor do abono ao usuário
print("O valor do seu abono no fim do mes sera de R$ {:.2f}".format(abono))