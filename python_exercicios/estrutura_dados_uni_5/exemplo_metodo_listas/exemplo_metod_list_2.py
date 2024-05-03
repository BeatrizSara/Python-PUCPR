"""
Como declarar uma lista []
Exemplo:
lista de compras - tem varios itens
Para cada item  na lista de compras por exemplo
NÃO PODE -  Nao misture tipos de dados dentro de uma única lista
"""
# len() para ver a quantidade de elementos na lista - pode ser uma função, um método muito útil
frutas = ["banana", "maçã", "laranja"]

if len(frutas) == 0:
    print("Lista esta vazia")

else:
    print("Lista nao esta vazia")

print(len(frutas)) # Output/ Console: 3 

# Exemplo com a lista vazia:

frutas = []

if len(frutas) == 0:
    print("Lista esta vazia")

else:
    print("Lista nao esta vazia")

print(len(frutas))

# Exemplo usando range()

frutas = ["banana", "maçã", "laranja"]

for i in range(3):
    nova_fruta = input("Digite o noemde mais uma fruta: ")
    frutas.append(nova_fruta) # inclui no final da lista a nova fruta
    print(frutas)