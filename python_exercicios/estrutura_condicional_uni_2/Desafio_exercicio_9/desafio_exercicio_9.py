""" 
Desafio
Exercício de fixação 9: Crie um programa que simule um caixa eletrônico. O programa deverá perguntar ao usuário 
o valor do saque e depois informar quantas notas de cada valor serão fornecidas, a saber:
Notas disponíveis: 1, 5, 10, 50 e 100 reais.
Valor mínimo de saque: R$ 10,00.
Valor máximo de saque: R$ 600,00.
Exemplo: 55 reais - saque % 50 - se dividir 55/50 - vai sobrar 5 
  55| 50
- 50  1
  05 - sobrou 5 entao, sobra = (saque(55) - sobra(5)) / 50 ---  50 / 50 = 1 (uma nota de 50 reais ) 
"""
import os # importando para usar função de limpar o terminal
import time
# Definindo valores disponiveis e limites de saque 
notas_disponiveis = [1, 5, 10, 50, 100]
valor_minimo  = 10
valor_maximo = 600
os.system("cls") # Função para limpar o terminal 
# Solicitar o valor do saque ao usuario 
print("Quanto deseja sacar? ")
print("Segue informações importantes")
print("Valor mínimo de saque - R$ 10,00")
print("Valor máximo de R$ 600, 00")
os.system("cls") 
saque  = float(input("Qual o valor do saque: "))
#Inicia número de notas em zero
n1=n5=n10=n50=n100 =  0
os.system("cls")
if saque < 10  or saque > 600:
    print("Infelizmente o valor informado é inválido")
    print("Deve informar um valor entre R$10,00 e R$600,00")
else: # Inicia o bloco de código a ser executado se o valor do saque estiver dentro dos limites permitidos.
# A partir daqui, o código verifica quantas notas de cada valor são necessárias para o saque, começando pelas notas de maior valor (R$100) até as de menor valor (R$1)    
    if saque >= 100: # Verifica se o valor restante a ser distribuído é maior ou igual a R$100.
        sobra = saque % 100 #  Calcula o valor restante após distribuir o máximo possível de notas de R$100.
        n100 = int((saque - sobra)/100)
        saque = sobra
        
    if saque >= 50:
        sobra = saque % 50
        n50 = int((saque - sobra)/50)
        saque = sobra
    
    if saque >= 10:
        sobra = saque % 10
        n10 = int((saque - sobra)/10)
        saque = sobra
    
    if saque >= 5:
        sobra = saque % 5
        n5 = int(( saque - sobra)/5)
        saque = sobra
        
    if saque >= 1:
        n1 = int(saque)

# O código imprime  a quantidade  de cada nota necessaria para o saque
print("Notas de 100:{}".format(n100))
print("Notas de 50: {}".format(n50))
print("Notas de 10: {}".format(n10))
print("Notas de 5: {}".format(n5))
print("Notas de 1: {}".format(n1))