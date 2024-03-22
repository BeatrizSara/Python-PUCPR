""" 
Exemplo de aplicação 3: Elabore um programa que solicite ao usuário seu ano de nascimento e calcule sua idade. 
Para ser mais assertivo, também deve perguntar se o usuário já fez aniversário neste ano e analisar a influência dessa informação no cálculo da idade.
"""
ano_nascimento = int(input("Informe seu ano de nascimento: "))
ano_atual = 2024
idade = ano_atual - ano_nascimento

resposta = str(input("Já fez aniversario nesse ano?"))

if resposta == "Não":
    idade -= 1 

print("Se voce é de {}, sua idade atual é {}".format(ano_nascimento, idade))