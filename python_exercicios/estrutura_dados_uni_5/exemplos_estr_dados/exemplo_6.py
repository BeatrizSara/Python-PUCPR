""" 
Exemplo de aplicação 6: Elabore um programa que concatene tuplas.
"""
endereco_puc = ("Rua Imaculada Conceição", 1555, "Prado Velho", "Curitiba", "PR")
print(id(endereco_puc))
endereco_puc += ("Brazil",)  # uma tupla com um único dado deve ser declarada com uma vírgula no fim; 
                             # caso contrário, o Python se confundirá e não entenderá que isto se trata de uma tupla
print(endereco_puc)
print(id(endereco_puc))