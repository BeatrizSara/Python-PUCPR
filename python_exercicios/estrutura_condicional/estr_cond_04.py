""" 
Exemplo de aplicação 4: Elabore um programa que solicite ao usuário as notas de determinada disciplina escolar e calcule a média. 
Se a média for maior ou igual a 7, deve mostrar que o estudante foi aprovado. Caso contrário (isto é, se a nota for menor do que 7), 
mostre uma mensagem ao estudante informando-o que foi reprovado.
"""

nota_1 = float(input("Primeira nota: "))
nota_2 = float(input("Segunda nota: "))
nota_3 = float(input("Terceira nota: "))
nota_4 = float(input("Quarta nota: "))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if media >= 7.0:
    print("Aluno APROVADO")
    print("Sua media foi {:.1f}".format(media))
    
else:
    print("Aluno REPROVADO")
    print("Sua media foi {:.1f}".format(media))