""" 
Escopo de função

E qual é o escopo de uma função? Como todo bloco em Python, seus limites começam a partir 
do símbolo de dois-pontos (:) e terminam quando o código deixa de estar indentado, voltando ao nível de arquivo.

Outra questão relacionada a escopo é o tempo de vida das variáveis criadas dentro da função. Uma variável criada 
em uma função tem seu tempo de vida limitado ao seu escopo. Além disso, ela tem precedência de acesso frente a uma 
variável externa ao escopo, mesmo tendo o mesmo nome. Teste este código:  
"""
def minha_funcao():
    x = 10 # linha 10
    print(f"Valor de x dentro da função: {x}")
 
x = 20
minha_funcao()
print(f"Valor de x fora da função: {x}")

# Valor de x dentro da função: 10

# Valor de x fora da função: 20

#Espere! Duas variáveis chamadas “x”? Confuso, não é? Pois então: essa diferença ocorre pela precedência da variável 
# criada com o mesmo nome dentro do escopo da função. No caso da remoção da linha 10, a variável pública x estaria visível 
# dentro da função minha_funcao(), gerando o seguinte resultado:

def minha_funcao():
    print(f"Valor de x dentro da função: {x}")
 
x = 20
minha_funcao()
print(f"Valor de x fora da função: {x}")

# Valor de x dentro da função: 20

# Valor de x fora da função: 20