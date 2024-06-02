""" 
Chamando uma função dentro de outra função (encadeamento)
----------------------------------------------------------------------------------------------
As funções podem ter chamadas encadeadas, de qualquer lugar, 
inclusive de dentro do corpo de outra função. 
Isso corrobora o conceito de modularizar os códigos o máximo possível, 
devendo uma função executar, normalmente, uma única tarefa.
----------------------------------------------------------------------------------------------
Exemplo de aplicação 5: Elabore um programa que, aplicando a fórmula de Bhaskara por funções, 
encontre as raízes de um polinômio do segundo grau, a saber:
"""

def delta(a, b, c): # é declarada a função delta()
    return b*b - 4*a*c

def bhaskara(a, b, c):
    d = delta(a, b, c)
    if d < 0 : # a função bhaskara() chama a função delta() para usar seu valor em seus cálculos internos
        print("As raízes são imaginárias")
        return 0, 0, False
    
    else:
        x1 = (-b + d ** 0.5) / 2*a
        x2 = (-b - d ** 0.5) / 2*a
        return x1, x2, True


result1 = bhaskara(1, 3, 1)
if result1[2]:
    print(f"As raízes são {result1[0]} e {result1[1]}")
    
result2 = bhaskara(1, 2, 1)
if result2[2]:
    print(f"As raízes são {result2[0]} e {result2[1]}")
    
result3 = bhaskara(1, 1, 1)
if result3[2]:
    print(f"As raízes são {result3[0]}e {result3[1]}")
    
""" 
Na linha 13, é declarada a função delta(). Na linha 18, a função bhaskara() chama a função delta() 
para usar seu valor em seus cálculos internos. Dessa forma, outro local no código que precise usar 
o valor de delta pode chamar a mesma função, não precisando refazer esse cálculo.
"""