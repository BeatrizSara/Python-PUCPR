""" 
Exemplo de aplicação 6: Leia o conteúdo do arquivo “pessoa.json” e armazene-o em uma variável chamada dados_lidos.
"""
#Como temos que ler os dados do arquivo json (mais especificamente, precisaremos usar a função load()), 
# precisaremos primeiro importar o módulo json.
import json                                                 # Como poderemos ter caracteres especiais (isto é, com acentos), usamos também o parâmetro encoding="utf-8" para evitarmos qualquer tipo de erro.
with open("pessoa.json", "r", encoding="utf-8") as arquivo: # Como temos que ler os dados do arquivo json (mais especificamente, precisaremos usar a função load()), precisaremos primeiro importar o módulo json.
    dados_lidos = json.load(arquivo) #usando a função json.load() para ler o conteúdo do arquivo JSON aberto e armazená-lo na variável dados_lidos
print(dados_lidos) #Finalmente, mostramos o conteúdo do arquivo lido (que agora é um dicionário) com o print(). Perceba que alguns comportamentos se repetem: o bloco de leitura do arquivo com o with, 
                   # e a abertura do arquivo em modo de leitura (“r”).

# A função load() carrega o conteúdo do arquivo JSON e converte-o em uma estrutura de dados Python, como um dicionário ou uma lista, dependendo do conteúdo do arquivo JSON.'
