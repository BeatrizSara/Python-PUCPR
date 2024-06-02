"""  """

frutas = ["banana", "maçã", "laranja", "melão", "abacaxi", "melancia"]
# Forma de navegar pelos subindices
print(frutas[2:5]) # Vai considerar os indices [2]laranja até o [4]abacaxi, pois o 5 nao repete 
frutas.sort() # Ordenar os elementos
print(frutas [-3:-1] ) # Vai considerar o [-3] melao, até [-2] abacaxi e nao considera a melancia [-1]