""" Continuação do raciocinio do exemplo_02.py """

frutas = ["banana", "maça", "laranja", "melão", "Abacaxi", "melancia"]
print(frutas)

frutas.reverse() # Inverte os elementos da lista, mas nao organiza em ordem alfabetica, 
                 # apenas analisa qual a ordem que a lista ja esta e a inverte
print(frutas)

frutas.sort() # Coloca em ordem alfabetica
print(frutas)

lista_antiga = frutas.copy() # frutas.copy() para chamar o clear com segurança 
frutas.clear() # Limpa a lista
print(frutas)

frutas.append("framboesa") # Incluir um elemento na lista frutas
print(frutas)

frutas.extend(["abacate", "mamão"]) # Vai ser uma outra lista composta por outos novos elementos
print(frutas)                       # .extende([]) - pode incluir mais de um elemento na lista
                                    # Entao ao inves de inlcuir pelo append -  um nome, um elemento novo na lista
                                    # Posso usar o extend([]) - para incluir mais de um nome de fruta ao mesmo tempo, simultaneamente

# frutas.remove("chinelo") - remove serve para remover um elemento da lista.  
# print(frutas)              - Mas nao tem chinelo na lista para ser removido -  resultando em erro quando rodar o programa

# NESTE CASO POSSO FAZER UM TESTE PARA VERIFICAR SE TEM OU NAO:
# if "chinelo" in frutas: # Verificar Se Chinelo esta na(in) lista das frutas
#    frutas.remove("chinelo")
# else:
# print("Elemento nao esta na lista")

elemento = "abacate" # nome do elemento que sera removido da lista de frutas

if elemento in frutas:
    resultado = frutas.remove(elemento) # Tem abacate na lista, entao sera removido da lista
    resultado2 = frutas.pop([0]) # pop -> posso salvar o resultado daquilo dentro de alguma operacao
    print(resultado2) # -> tem que informar no pop - qual é o indice que eu desejo remover da lista e nao o nome do elemento que fica em string ""
else:
    print("Elemento nao esta na lista")
    
print(frutas)

# Diferenca entre REMOVE e POP
# Remove - falo qual o valor que eu quero remover
# Pop - falo qual que é o indice que quero remover frutas[0] ou frutas[3] por exemplo