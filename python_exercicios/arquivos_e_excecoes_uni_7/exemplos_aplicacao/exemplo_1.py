""" 
Exemplo de aplicação 1: Crie uma aplicação a qual pede o nome do usuário. 
Em seguida, salve em um arquivo chamado “nome.txt” o nome desta pessoa.
"""
nome = input("Digite o seu nome: ")

with open("nome.txt", "w") as f:
    f.write(nome)
    
# Veja novamente o bloco with open("nome.txt", "w") as f:. 
# Ele é responsável por abrir o arquivo "nome.txt" no modo de escrita ("w") 
# em uma variável chamada f. Utilizando esta variável f, chamamos o método 
# write() para escrever o conteúdo da variável nome no arquivo.