""" 
Ordenar os elementos
LISTA DE STRINGS - fica em ordem alfabetica
LISTA DE NÚMEROS - fica em ordenacao numerica
"""

frutas = ["banana", "maça", "laranja", "melão", "Abacaxi", "melancia"]
print(frutas) # primeiro print  que vai mostar a lista na ordem que esta 

frutas.sort() 
print(frutas) # Ele vai ordenar aquela lista - ordem alfabetica por ser string
              # Ele ordena ja dentro dela
              # entao nao precisa fazer -> frutas = frutas.sort()
              # ['Abacaxi', 'banana', 'laranja', 'maça', 'melancia', 'melão']


# sorted(frutas)  # outra forma de fazer isso tbm é com sorted: 
# frutas.sort()   # para ordenar a lista - ele ordena ja dentro dela, 
                
frutas.reverse() # Vai inverter os elementos da lista. Tal como ela esta agora.
print(frutas)    # Vai inverter a lista que ficou na ordem alfabetica abc
                 # Ficando: ['melão', 'melancia', 'maça', 'laranja', 'banana', 'Abacaxi']
                 
frutas.clear() # Vai limpar a lista, deixando ela vazia [] sem nada
print(frutas)

frutas.append("framboesa") # O append vai incluir mais um elemento na lista
print(frutas)

