"""
Parte 2.
Bom, além do código ficar longo temos um outro problema: repetir esta lógica do cálculo do IMC em 
três lugares diferentes leva a erros e dificuldade de manutenção. Se quiséssemos mudar qualquer 
coisa dentro daqueles loops que calculam o IMC, o precisaríamos fazer ao menos três vezes. 
É um trabalho bastante repetitivo, não acha? Agora, veja como seria o mesmo código com o uso de 
uma função somente nossa, chamada de calcular_imc(). Veja, em negrito, as linhas que mudaram:
"""
def calcular_imc(lista_de_pessoas):# parte do bloco de código que mudou
    for pessoa in lista_de_pessoas:
        altura = pessoa['altura']
        peso = pessoa['peso']
        imc = peso / (altura ** 2)
        print(f'O IMC de {pessoa["nome"]} é {imc:.2f}') # mudou até aqui

# Dados das pessoas em formato de lista de dicionários
pessoas = [
    {'nome': 'João', 'altura': 1.75, 'peso': 70},
    {'nome': 'Maria', 'altura': 1.60, 'peso': 55},
    {'nome': 'Carlos', 'altura': 1.80, 'peso': 90}
]
calcular_imc(pessoas) # parte do código que mudou

print("Continuando o cálculo para uma nova lista de pessoas.")
print("Este aqui é só um print para demonstrar o código.")

# Dados das pessoas em formato de lista de dicionários
novas_pessoas = [
    {'nome': 'Cézar', 'altura': 1.78, 'peso': 79},
    {'nome': 'Marta', 'altura': 1.61, 'peso': 52},
    {'nome': 'Ana', 'altura': 1.65, 'peso': 70}
]
calcular_imc(novas_pessoas) # parte do código que mudou

print("Agora, vamos para a lista final.")

# Dados das pessoas em formato de lista de dicionários
mais_pessoas = [
    {'nome': 'Kauane', 'altura': 1.53, 'peso': 51}
]
calcular_imc(mais_pessoas) # parte do código que mudou

""" 
Perceba algumas coisas:

A quantidade de linhas a menos no código.
Que podemos chamar a função calcular_imc() quantas vezes quisermos, 
e em qualquer outra parte do código sem precisar copiar e colar aquele for.
O conceito de caixa-preta: não importa a linha que chamemos a função calcular_imc(),
ela fará o cálculo sem precisarmos saber como ela faz isso.
"""