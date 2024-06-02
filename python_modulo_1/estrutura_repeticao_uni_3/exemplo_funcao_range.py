""" 
Exemplo de aplicação 3: Elabore um programa que calcule o fatorial de um número, 
exibindo a informação de como é feito o cálculo. 
Exemplo: “O valor do fatorial de 5 é igual a 120. Expressão: 5*4*3*2*1”. 
"""
fatorial = 1
expressao = "Expressão: "# variável será usada para construir a expressão do fatorial.
numero = int(input("Informe um numero para código fatorial: "))

for i in range(numero, 0, -1):
    fatorial += i 
    expressao += str(i)
    if i > 1:
        expressao += "*"
print(f"O valor do fatorial de {numero} é {expressao}")