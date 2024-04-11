""" 
Exercício de fixação 8: Crie um programa que gere a série de Fibonacci 
enquanto o valor for menor que um valor informado pelo usuário. 
Observação: série de Fibonacci = 0, 1, 1, 2, 3, 5, 8 ,13, 21, 34, 55, ... 
é formada por 0, 1 e, partir deste ponto, sempre será a soma dos dois valores anteriores.
"""
valor = 0

while True:
    
    max = int(input("Informe um valor limite: "))
    num_1 = 0
    num_2 = 1
    serie = "0, 1"
    
    while valor < max:
        valor = num_1 + num_2
        if valor < max:
            num_1 = num_2
            num_2 = valor
        serie += ", " + str(valor)
        valor = num_1 + num_2
    
    print("Serie de Fibonacci: {}".format(serie))