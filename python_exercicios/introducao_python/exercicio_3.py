"""
Exercício de fixação 3: Elabore um algoritmo que solicite ao usuário seu ano de nascimento e
calcule sua idade com relação ao ano de 2023, sendo que o usuário já fez aniversário nesse ano.
"""

# Solicita o ano de nascimento do usuario
ano_nascimento = int(input("Informe seu ano de nascimento: "))

ano_atual = 2023
idade = ano_atual - ano_nascimento

print(f"A idade atual é {idade}")