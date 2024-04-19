""" Exemplo de aplicação 8: Elabore um programa que faça uso de uma tupla chamada Endereco, contendo dados nomeados."""

from collections import namedtuple

endereco = namedtuple("Endereço", ["logadouro", "numero", "bairro", "cidade", "estado"])

endereco_puc = endereco(logadouro="Rua Imaculada Conceição", numero=1555, bairro="Prado Velho", cidade="Curitiba", estado="PR")
print(f"Endereço:{endereco_puc[0]}") # A partir do índice, como se fosse uma lista ou como se fosse uma tupla qualquer 
print(f"Número: {endereco_puc.numero}") # ---
print(f"Bairro: {endereco_puc.bairro}") # ---\ A partir do nome daquele elemento
print(f"Cidade: {endereco_puc.cidade}") # ---/ Esta maior legibilidade trazida ao código é importante, especialmente ao trabalhar em um projeto grande.
print(f"Estado: {endereco_puc.estado}") # ---