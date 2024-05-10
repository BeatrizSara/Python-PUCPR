""" Exemplo de aplicação 2: Usando o exemplo de aplicação 1, leia o nome salvo no arquivo “nome.txt”, 
mostrando cada caractere em uma linha separada."""

with open("nome.txt", "r") as f:
    conteudo = f.read()
    
    for letra in conteudo:
        print(letra)
        
# Veja que, como estamos lendo o arquivo, agora o bloco é with open("nome.txt", "r") as f:. 
# Aquele "r" indica que estamos abrindo o arquivo "nome.txt" no modo de leitura. 
# O conteúdo do arquivo é lido e armazenado na variável conteudo.
#Depois, usamos um for para mostrar cada letra dentro de uma única linha.