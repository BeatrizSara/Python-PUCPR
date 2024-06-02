""" 
Exemplo 1 Validação de dados em Exceção
"""
try:
    num = int(input("Digite um número: "))
except:
    print("Valor inválido")