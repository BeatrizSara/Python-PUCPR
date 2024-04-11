""" Forme um atabuada utilizando o comando for 
de modo a economizar códigos, sem utilizar muitas linhas"""

numero = int(input("Qual tabuada deseja: "))

for i in range(0, 11):
    resultado = numero*i
    print("{} x {} = {}".format(numero, i, resultado))