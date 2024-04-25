""" 
Criando a nossa própria função: parâmetros e retornos . Parte 1.

E se quiséssemos criar a nossa própria função? Vamos pensar primeiro em um cenário em que criar uma 
função pode ser útil. Sendo assim, pensemos em um cenário em que precisamos calcular 
o IMC (Índice de Massa Corporal) para uma lista de pessoas.
"""
# Dados das pessoas em formato de lista de dicionários
pessoas = [
    {'nome': 'João', 'altura': 1.75, 'peso': 70},
    {'nome': 'Maria', 'altura': 1.60, 'peso': 55},
    {'nome': 'Carlos', 'altura': 1.80, 'peso': 90}
]

# Cálculo do IMC para cada pessoa
for pessoa in pessoas:
    altura = pessoa['altura']
    peso = pessoa['peso']
    imc = peso / (altura ** 2)

    print(f'O IMC de {pessoa["nome"]} é {imc:.2f}')

print("Continuando o cálculo para uma nova lista de pessoas.")
print("Este aqui é só um print para demonstrar o código.")

# Dados das pessoas em formato de lista de dicionários
novas_pessoas = [
    {'nome': 'Cézar', 'altura': 1.78, 'peso': 79},
    {'nome': 'Marta', 'altura': 1.61, 'peso': 52},
    {'nome': 'Ana', 'altura': 1.65, 'peso': 70}
]
# Cálculo do IMC para cada pessoa
for pessoa in novas_pessoas:

    altura = pessoa['altura']
    peso = pessoa['peso']
    imc = peso / (altura ** 2)
    print(f'O IMC de {pessoa["nome"]} é {imc:.2f}')

print("Agora, vamos para a lista final.")

# Dados das pessoas em formato de lista de dicionário
mais_pessoas = [
    {'nome': 'Kauane', 'altura': 1.53, 'peso': 51}
]

# Cálculo do IMC para cada pessoa
for pessoa in mais_pessoas:
    altura = pessoa['altura']
    peso = pessoa['peso']
    imc = peso / (altura ** 2)
    print(f'O IMC de {pessoa["nome"]} é {imc:.2f}')
    
""" 
Este código funciona e vai calcular o IMC para cada pessoa na lista. Porém, perceba algumas coisas:

1. Temos três listas diferentes de pessoas (pessoas, novas_pessoas e mais_pessoas).
2. Para cada uma dessas listas temos exatamente a mesma lógica dentro de um loop for. 
Em outras palavras, veja que o código dentro de cada loop for é copiado e colado três vezes.
3. Entre cada uma dessas listas de pessoas temos print() que mostram mensagens diferentes na tela. 
No lugar deste print() poderia ser qualquer outro código - a ideia aqui é a de demonstrar um caso 
em que usar um novo loop não resolveria necessariamente o problema. 
"""