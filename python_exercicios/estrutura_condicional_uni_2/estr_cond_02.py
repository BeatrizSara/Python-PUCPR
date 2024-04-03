""" 
Seleção Simples
Exemplo de aplicação 2: Elabore um programa que solicite ao usuário as notas de determinada disciplina escolar e calcule a média. 
Se a média for maior ou igual a 7, deve mostrar que o estudante foi aprovado. Vamos pensar em um exemplo direto em Python? 
Sugiro que você tente implementar por si só, e somente depois consultar a resposta aqui embaixo.
"""
disciplina = str(input("Qual dsiciplina deseja verificar a media: "))
nota_1 = float(input("Informe sua nota um: "))
nota_2 = float(input("Informe sua nota dois: "))
nota_3 = float(input("Informe sua nota três: "))
nota_4 = float(input("Informe sua nota quatro: "))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if media >= 7.0:
    print("Estudante APROVADO")

print("Sua media em {} foi {:.1f}".format(disciplina, media))