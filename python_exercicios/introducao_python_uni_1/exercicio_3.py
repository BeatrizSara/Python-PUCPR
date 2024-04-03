"""
Exercício de fixação 3: Elabore um algoritmo que solicite ao usuário seu ano de nascimento e
calcule sua idade com relação ao ano de 2023, sendo que o usuário já fez aniversário nesse ano.
"""

# Solicita o ano de nascimento do usuario
ano_nascimento = int(input("Informe seu ano de nascimento: "))

# Calcula sua idade com relação ao ano de 2023
ano_atual = 2023
idade = ano_atual - ano_nascimento

# Informa ao usuário sua idade atual
print(f"A idade atual é {idade}")

""" 
Entrada: Ano de nascimento

Saída: idade ate o ano 2023

Passos: 
    - Peça ao usuario que informe o ano de nascimento
    - Guarde a resposta do usuario em uma variavel "ano_nascimento"
    - idade = ano_atual - ano_nascimento
    - Exiba a variavel "idade" para o usuario

"""