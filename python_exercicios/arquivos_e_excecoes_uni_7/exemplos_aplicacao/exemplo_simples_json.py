""" 
Arquivos JSON
Agora, e se quiséssemos salvar os arquivos de uma forma padronizada? Isto é: e se quiséssemos transferir dados entre diferentes sistemas seguindo algum tipo de padrão internacional em que toda empresa de tecnologia saberia (ou deveria saber) como funciona?

É aí que entram os arquivos JSON. JSON (JavaScript Object Notation) é um formato leve e de fácil leitura utilizado para a troca de dados entre sistemas. Ele é amplamente utilizado na comunicação entre aplicativos web e é suportado por várias linguagens de programação, incluindo o Python.

O JSON é baseado em uma estrutura de dados composta por pares de chave e valor. Esses pares são organizados em uma sintaxe simples e legível, permitindo representar informações de forma estruturada. A estrutura básica do JSON consiste em objetos e arrays (vetores, ou listas).

Objetos: são delimitados por chaves {} e consistem em uma coleção não ordenada de pares chave-valor. Cada chave é uma string única que identifica o valor associado a ela. Os pares chave-valor são separados por vírgulas.
Arrays: são delimitados por colchetes [] e podem conter uma lista ordenada de valores. Os valores em um array podem ser de qualquer tipo válido do JSON, incluindo strings, números e outros arrays. Os elementos do array são separados por vírgulas.
Veja só um exemplo:
"""

{
    "nome": "João",
    "idade": 25,
    "cidade": "Curitiba",
    "frutas_favoritas": [
        "maçã",
        "banana",
        "laranja"
    ]
}