""" 
Exemplo de aplicação 1: Elabore um programa que simule 
o cadastro de telefones com dicionário como uma agenda, 
exibindo, ao final, o dicionário.
"""
#Key = o valor q tem na variavel nome
#Value = o valor q tem na variavel telefone

agenda = {} # dicionario vazio com nome agenda
print("*** Cadastro de telefones ***")
while True: # Iniciamos um laço de repetição infinito, que só será interrompido quando o usuário decidir.
    # Solicitamos ao usuário para que insira o nome e o número de telefone do contato. 
    # Guardamos estas informações nas variáveis chamadas contato e telefone, respectivamente.
    contato = input("Digite o nome do contato: ") # Contato é a chave com o nome que o usuario vai informar
    telefone = input("Digite o telefone do contato: ") # Telefone é o valor do número do contato que o usuario vai informar 
    agenda[contato] = telefone #  Adicionamos o telefone no dicionário agenda. A chave para encontrarmos o telefone será o contato.
    if input("Deseja cadastrar um novo contato (s/n): ") == "n":
        break # Perguntamos ao usuário se ele deseja cadastrar um novo contato. Se o usuário digitar "n", o laço é interrompido.
print(agenda) # Mostramos o dicionário agenda, mostrando todos os contatos e seus respectivos números de telefone que foram cadastrados.

# Este dicionário será usado para armazenar pares de chave-valor, 
# onde: 
# A chave é o nome do contato
# O valor é o número de telefone do contato.