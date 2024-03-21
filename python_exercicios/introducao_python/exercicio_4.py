""" 
Exercício de fixação 4: Elabore um algoritmo que solicite ao usuário o nome de uma disciplina e suas quatro notas bimestrais. 
O algoritmo deve calcular a média dessas notas e exibir uma mensagem informando que a média da disciplina nome é média.
"""
# Solicita o nome da disciplina ao usuário
disciplina = str(input("Informe qual disciplina deseja verificar: "))
# Solicita as notas da dsiciplina ao usuário
nota_1 = float(input("Informe a nota um: "))
nota_2 = float(input("Informe a nota dois: "))
nota_3 = float(input("Informe a nota tres: "))
nota_4 = float(input("Informe a "))

# Calcula a media das notas do usuário
media = (nota_1+nota_2+nota_3+nota_4) / 4

# Informa a media da disciplina do usuario
print(f"A média da disciplina {disciplina} é {media:.2f}")

""" 
Entrada: Nome de uma disciplina e notas bimestrais

Saída:  Noem da disciplina 
        Média da disciplina

Passos:
    - Peça ao usuario que informe uma disciplina
    - Guarde o que o usuario digitou na variavel "disciplina" 
    - peça ao usuario para informar a nota um da disciplina
    - Guarde o que o usuario digitou na variavel "nota_1"
    - peça ao usuario para informar a nota dois da disciplina
    - Guarde a resposta do usuario na variavel "nota_2"
    - peça ao usuario para informar a nota tres da disciplina
    - Guarde o que o usuario digitou na variavel "nota_3"
    - peça ao usuario para informar a nota quatro da disciplina
    - Guarde o que o usuario digitou na variavel "nota_4"
    - media = (nota_1+nota_2+nota_3+nota_4) / 4
    - Exiba a variavel "disciplina" e "media" para o usuario
"""