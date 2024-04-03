""" 
Exercício de fixação 8: Crie um programa que solicite ao usuário as quatro notas bimestrais de uma matéria 
e o número de faltas. Informe se o aluno foi aprovado ou reprovado, bem como o motivo, a saber:
A média anual é 7.
A disciplina possui 40 aulas.
O mínimo exigido é 75% de presença.
"""
print("=== Sistema de Verificação de  Aprovação === ")
nota_1 = float(input("Nota 1º bimestre: "))
nota_2 = float(input("Nota 2º bimestre: "))
nota_3 = float(input("Nota 3º bimestre: "))
nota_4 = float(input("Nota 4º bimestre: "))

faltas = int(input("Informe o número de faltas: "))
media_anual  = (nota_1 + nota_2 + nota_3 + nota_4)/ 4
presenca = (40 - faltas) / 40*100

if media_anual >= 7.0 and presenca >= 7.5:
    if (40 - faltas) >= 0.75 * 40:
        print("Aluno Aprovado")
    elif media_anual >= 7:
        print("Aluno reprovado por falta")
        print("Presença anual inferior a 75%")
    elif presenca >= 0.75 :
        print("Aluno reprovado por ")
    else:
        print("Aluno reprovado por falta ( Presença inferior a 75%)")

elif media_anual >= 7:
    print("Aluno reprovado por media (media anual inferior a 7.0)")