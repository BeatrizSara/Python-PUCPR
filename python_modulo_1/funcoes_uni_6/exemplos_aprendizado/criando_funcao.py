""" 
Criando uma função

A criação de uma função em Python sempre segue uma mesma “receita”. 
Sendo assim, sempre criamos as funções em Python com a palavra-chave def, 
seguida do nome da função, e os parâmetros entre parênteses () e, no final, 
dois-pontos. Veja a sintaxe geral de uma função:

def nomedafuncao(param1, param2, ...):
    (...)
    return resultado
    
"""
# Vamos pensar em um exemplo de função que calcula a área de um triângulo. Veja só:

def calcular_area_triangulo(base, altura):

    area = (base * altura)/2
    return area

""" 
Perceba os seguintes itens considerando a “receita”:
--------------------------------------------------------------------------------------
1. Primeira linha: 
def calcular_area_triangulo(base, altura):

a. Esta linha é a declaração da função.
b. A palavra def é usada para definir uma função em Python.
c. calcular_area_triangulo é o nome da função.
d. base e altura são os parâmetros que a função recebe.
---------------------------------------------------------------------------------------
2. Segunda linha: 
    area = (base * altura)/2

a.Esta linha calcula a área de um triângulo usando a fórmula da área de um triângulo, 
que é (base * altura) / 2.
b. O resultado é armazenado na variável area.
c. Usamos somente as variáveis que foram informadas como parâmetros na primeira linha 
desta função.
---------------------------------------------------------------------------------------
3. Terceira linha:
    return area

a.  Esta é a instrução de retorno da função.
b. Quando a função é chamada, ela calculará a área do triângulo com base nos valores de 
base e altura fornecidos e retornará esse valor para que o resto do algoritmo possa usá-lo.
"""

# Veja como a função que acabamos de definir pode ser chamada de diferentes formas com diferentes valores:
def calcular_area_triangulo(base, altura):
    area = (base * altura)/2
    return area

print("A área do triângulo é", calcular_area_triangulo(19, 10))
print("A área do triângulo é", calcular_area_triangulo(10, 3))
print("A área do triângulo é", calcular_area_triangulo(5, 5))
print("A área do triângulo é", calcular_area_triangulo(9, 7))
print("A área do triângulo é", calcular_area_triangulo(20, 14))