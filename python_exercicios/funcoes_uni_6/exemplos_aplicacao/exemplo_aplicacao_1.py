""" 
Exemplo de aplicação 1: Elabore um programa que cadastre contatos de uma agenda telefônica. 
A função de cadastro deve ser realizada dentro de uma função chamada inserir, que recebe 
como parâmetros o nome e o telefone do contato, bem como a agenda de contatos.
"""

agenda_telefonica = {}

def inserir(nome, telefone, agenda):
    agenda[nome] = telefone
    
while True:
    
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    inserir(nome, telefone, agenda_telefonica)
    
    if input("Gostaria de adicionar um nome contato? (s/n) ")  == "n":
        break
    
print(agenda_telefonica)

""" 
Como pode ser visto no exemplo, a função inserir() não retorna valores, uma vez que sua função não exige isso. 
Entretanto, se ela for expandida para verificar se um nome já existe na lista de contatos e perguntar se deseja 
modificar o telefone cadastrado, poderia retornar true ou false, indicando que foi feita uma inclusão ou não na agenda. 

Vamos ver como esse código ficaria neste caso?
o exemplo 2 se localiza no documento exemplo de aplicacao  2
"""