# Acessar os elemtentos de uma lista/vetor
frutas = ["banana", "maça", "laranja", "melão", "Abacaxi", "melancia"]
# Consegue acessar cadacelemento, informando qual indice eu gostaria de acessar
print(frutas[0]) # Acessar o primeiro elemento
print(frutas[1]) # Acessar o segundo elemento
print(frutas[2]) # Acessar o terceiro elemento
print(frutas[3]) # Acessar o quarto elemento
print(frutas[4]) # Acessar o quinto elemento
print(frutas[5]) # Acessar o sexto elemento

# O que pode dar erro - colocar um numero dento do indice 
# que nao corresponde a quantidade de elementos contidos 
# na lista[]
# Exemplo 2 - Erros : print(frutas[50]) - o vetor possui apenas 6 elementos  e nao 50.

# Exemplo 3 - indice negativo
# E se tentar acessar um elemento como [-1]? Vai aparecer a melancia a mais. melancia, melancia
print(frutas[-1]) # -1 CONTA de TRÁS PRA FRENTE - o ultimo elemento - melancia
print(frutas[-2]) # Penultimo elemento - ABACAXI
print(frutas[-3]) # Vai mostrar o antepenultimo elemento - MELÃO
print(frutas[-4]) # - LARANAJA
print(frutas[-5]) # - MAÇÃ

# Exemplo 4 - quando se coloca no print(frutas[ : ]) - um indice c/ outro indice
# Ele vai pegar uma Sublista contendo todos os elementos naquele intervalor
# Vai do indice 2 até o 5 ou seja indice 2 é Maça - que na ordem é 1
print(frutas[2:5]) # Indice 2 = LARANJA até o indice 5 = MELANCIA

# POSICAO DE CADA INDICE 
# Possui 6 elementos
# BANANA - [0] 
# MAÇA - [1]
# LARANJA - [2]             Pode acessar esses indices de forma negativa [-n]
# MELAO - [3]                           - É de TRAS PARA FRENTE
# ABACAXI - [4]
# MELANCIA - [5]

# Exemplo 5 
print(frutas[-3:-1]) # Vai acessar Melao[-3] - Abacaxi[-2] - e NÃO Considera o -1 - Melancia