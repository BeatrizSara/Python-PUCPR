""" 
An example that uses of the list methods:
Esses métodos são úteis para adicionar, remover, ordenar e manipular elementos em listas de forma eficiente em Python.
"""
# 1. append(elemento): Adiciona um elemento ao final da lista.

lista = [1,2,3]
lista.append(4)
print(lista) # Output: [1, 2, 3, 4]

# 2. extend(iterável): Adiciona os elementos de um iterável (como outra lista) ao final da lista atual.
lista1 = [1,2,3]
lista2 = [4,5]
lista1.extend(lista2)
print(lista1) # Output: [1, 2, 3, 4, 5]

# 3. insert(posição, elemento):  Insere um elemento em uma posição específica na lista.
lista = [1,2,3]
lista.insert (1,4)
print(lista) # Output: [1, 4, 2, 3]

# 4. remove(elemento): Remove a primeira ocorrência do elemento na lista.
lista = [1,2,3,2]
lista.remove(2)
print(lista) # Output: [1, 3, 2]

# 5. pop([índice]): Remove e retorna o elemento na posição especificada (ou o último elemento se nenhum índice for fornecido).
lista = [1,2,3]
elemento = lista.pop(1)
print(elemento) # Output: 2
print(lista) # Output: 2

# 6. index(elemento[, start[, end]]): Retorna o índice da primeira ocorrência do elemento dentro dos limites opcionais de start e end.
lista = [1,2,3,2]
indice = lista.index(2)
print(indice) # Output: 2

# 7. count(elemento): : Retorna o número de ocorrências do elemento na lista.
lista = [1,2,3,2]
vezes = lista.count(2)
print(vezes) # Output: 2

# 8. sort(key=None, reverse=False): Ordena a lista em ordem crescente (ou decrescente se reverse=True), 
#  opcionalmente usando uma função de chave para personalizar a ordenação.
lista = [3,1,2]
lista.sort()
print(lista) # Output: [1, 2, 3]

# 9. reverse():  Inverte a ordem dos elementos na lista.
lista = [1,2,3]
lista.reverse()
print(lista) # Output: [3, 2, 1]

# 10. clear(): Remove todos os elementos da lista, deixando-a vazia.
lista = [1,2,3]
lista.clear()
print(lista) # Output: []