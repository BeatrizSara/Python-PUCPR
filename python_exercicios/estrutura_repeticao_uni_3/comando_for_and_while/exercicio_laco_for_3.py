""" 
Exercício de fixação 3: Crie um programa que receba um texto digitado pelo usuário 
e o imprima apenas com consoantes, removendo as vogais. 
Observação: desconsiderar letras maiúsculas e acentos.
"""

frase = str(input("Digite um pequeno texto: "))
consoantes = ""
for letra in frase:
    if letra.lower() not in "aeiou":
        consoantes += letra
    
print(consoantes)