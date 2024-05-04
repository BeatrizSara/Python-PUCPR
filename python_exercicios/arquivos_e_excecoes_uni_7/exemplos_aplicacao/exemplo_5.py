""" 
Exemplo de aplicação 5: Salve o exemplo de JSON acima em um arquivo chamado “pessoa.json”.
"""
import json # importando o módulo json da biblioteca padrão do Python
# módulo que fornece funções para trabalhar com JSON. Sem isso, não conseguiremos ler e salvar dados em JSON.

# dicionário contendo várias informações sobre uma pessoa.
dados = {
    "nome": "João",
    "idade": 25,
    "cidade": "Curitiba",
    "frutas_favoritas": [
        "maçã",
        "banana",
        "laranja"
    ]
}

with open("pessoa.json", "w", encoding="utf-8") as arquivo: # abrindo um arquivo chamado “pessoa.json” em modo de escrita (“w”).
    json.dump(dados, arquivo, ensure_ascii=False) # usando a função json.dump() para escrever o conteúdo do dicionário dados no arquivo JSON aberto.
    
# encoding=”utf-8” - Foi definido esse parâmetro para garantir que caracteres especiais (como o “ã” e “ç”) sejam tratados corretamente

# A função dump() recebe três argumentos: o dicionário dados que será convertido em JSON, a variável arquivo onde os dados serão gravados 
# e o parâmetro ensure_ascii=False para permitir a codificação correta de caracteres não-ASCII (isto é, caracteres que não façam parte do alfabeto da língua inglesa)

""" 
Contexto: o código de caracteres ASCII era usado nos primeiros dias da Computação para mapear os caracteres em computadores. Ele possui 128 caracteres, incluindo letras maiúsculas e minúsculas, números e símbolos de pontuação.

Ainda que isto funcionasse bem para quem trabalhasse somente com dados em inglês, ele não é compatível com todos os alfabetos e símbolos especiais do mundo. Por isso, hoje é normal usarmos outro código mais amplo: o UTF-8 (Unicode). 
Ele é adequado para aplicações multilíngues e internacionais. Os emojis fazem também parte do UTF-8.

"""