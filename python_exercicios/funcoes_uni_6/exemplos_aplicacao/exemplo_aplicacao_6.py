"""
Documentando funções

Exemplo de aplicação 6: Tomando por base o exemplo de aplicação 4, 
elabore a documentação no padrão PEP 257 da função.
"""

def maior_menor(*numeros):
    """ 
    Recebe uma lista aleatória de números e calcula o maior e o menor deles
    :para numeros: lista de numeros a ser analisados
    :return: retorna o maior e o menor número da lista
    """
    maior = - 1000000
    menor = 1000000
    for numero in numeros:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    return maior, menor

""" 
Documentando funções 

Documentar os códigos é uma boa prática de desenvolvimento. Especificamente no caso de funções, 
a documentação dentro de um padrão específico permite, com ferramental extra, a criação de documentação 
automática gerada a partir das informações cadastradas. Da mesma forma, com o padrão correto, o PyCharm 
consegue ler internamente a descrição das funções, gerando uma ajuda que pode ser acessada internamente 
no projeto.
O desenvolvimento em Python é regido por alguns documentos de boas práticas, chamados Python Enhancement 
Proposals (PEPs). No caso da documentação, existe o padrão docstrings, registrado pelo PEP 257 - Docstring Conventions.
Se você estiver usando o PyCharm é possível gerar esta documentação de forma semiautomática. Para tanto, na primeira 
linha da função após ela estar completa, devem ser digitadas três aspas seguidas para comentário de várias linhas e 
pressionar Enter. Segue como exemplo o padrão criado automaticamente no PyCharm sobre a função delta() do exemplo anterior:

"""
def delta(a, b, c):
    """
 
    :param a:
    :param b:
    :param c:
    :return:
    """
    return b*b - 4*a*c

# Considerando o padrão criado, a função pode ser documentada como segue:

# def delta(a, b, c):
    """
    Calcula o valor de delta utilizado no cálculo de raízes de polinômios de segundo grau.
 
    :param a: Valor do primeiro termo do polinômio.
    :param b: Valor do segundo termo do polinômio.
    :param c: Valor do termo independente do polinômio.
    :return: Retorna as raízes calculadas e um booleano, indicando se o cálculo foi bem-sucedido.
    """
    #return b*b - 4*a*c

# É importante destacar que a linha 53 está em branco propositalmente: essa separação se faz 
# necessária para que a documentação exibida fique bem formatada. Posicionando o cursor sobre 
# a função delta ou sua chamada ao longo do algoritmo e pressionando a tecla F1, a documentação 
# que acabamos de criar será carregada automaticamente.

