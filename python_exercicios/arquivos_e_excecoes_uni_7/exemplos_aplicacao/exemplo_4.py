""" 
Exemplo de aplicação 4: Leia novamente o conteúdo do arquivo “nome.txt”. 
Agora, leia uma linha de cada vez, e mostre o conteúdo de cada linha na tela.
"""
with open("nome.txt", "r") as f:
    for linha in f.readlines():
        print(linha)

# Perceba que alguns comportamentos se repetem: o bloco de leitura do arquivo com o with, 
# e a abertura do arquivo em modo de leitura (“r”). 
# Agora, veja que o conteúdo do f.readlines() é uma lista de strings. 
# Cada string é uma linha do arquivo. 
# Como é uma lista, estamos usando o for para mostrar cada linha individualmente na tela para o usuário.