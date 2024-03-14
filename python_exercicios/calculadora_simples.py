""" 
Calculadora simples 
"""

primeiro_valor = float(input("Informe o primeiro valor: "))

segundo_valor = float(input("Informe o segundo valor: "))

 

soma = primeiro_valor + segundo_valor

subtracao = primeiro_valor - segundo_valor

multiplicacao = primeiro_valor * segundo_valor

divisao = primeiro_valor / segundo_valor

resto = primeiro_valor % segundo_valor

print(f"Soma:{soma:.0f}")
print(f"Subtração: {subtracao:.2f}")
print(f"Multiplicação: {multiplicacao:.2f}")
print(f"Divisao: {divisao:.2f}")
print(f"Resto: {resto}")