""" 
Exercício de fixação 5: Crie um programa que peça dois números ao usuário - o primeiro será o numerador e o segundo, o expoente. 
A saída do programa deve ser o resultado da operação: numerador elevado ao expoente. 
Observação: não use a função própria do Python que calcula automaticamente potência.
"""
numerador = int(input("Informe um número para numerador: "))
expoente = int(input("Informe um número para expoente: "))

resultado = 1
for i in range(expoente):
    resultado *= numerador # realizar o breakpoint para entender o que ocorre nessa etapa.

print("O resultado de {} elevado a {} é igual a: {}".format(numerador, expoente,  resultado))