""" 
Exemplo de aplicação 3: Salve dois números decimais em novas linhas do mesmo arquivo “nome.txt”.
"""

primeiro_numero = 1.01
segundo_numero = -2.95

with open("nome.text", "a") as f:
    f.write("\n" + str(primeiro_numero))
    f.write("\n" + str(segundo_numero))
    
# Viu que o bloco começa com with open("nome.txt", "a") as f:? Aquele "a" indica que somente estamos acrescentando dados no arquivo 
# sem apagar o que já tínhamos armazenado antes. É esta a diferença principal entre o modo "a" e "w".

# Depois, perceba que temos dois write(): eles servem para que armazenemos os dois números no arquivo. Perceba também duas coisas:

#   1. Tivemos que converter os números para texto primeiro com o str() (mais especificamente, com o str(primeiro_numero)  e str(segundo_numero)). 
# Isto era importante porque não somente conseguimos salvar strings no arquivo. Por isso, precisamos converter os números para strings antes de salvá-los no arquivo.

#   2. Perceba também que colocamos no início de cada escrita de arquivo um “\n”. Este caracter significa “line feed”, ou “quebra de linha”. Isto garante com que 
# salvemos cada número em uma linha separada.
