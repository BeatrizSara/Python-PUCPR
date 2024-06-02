""" 
Projeto pyhton - venda de ingressos para o tipo (comum/estudante)
"""
def calcular_preco(tipo):
    if tipo == "estudante":
        return 10
    elif tipo == "comum":
        return 20 
    else:
        print("Ingresso Inválido")
        return 0

capacidade_maxima = 100
ingressos_vendidos = 0

while ingressos_vendidos < capacidade_maxima:
    print(f"Foram vendidos {ingressos_vendidos} ingressos")
    ingressos_disponiveis = capacidade_maxima - ingressos_vendidos
    print(f"Temos {ingressos_disponiveis} ingressos disponíveis ")
    
    quantidade = int(input("Quantos ingressos deseja comprar: "))
    
    if quantidade > ingressos_disponiveis:
        print("Não temos essa quantidade de ingressos disponíveis")
        continue
    
    tipo = str(input("Qual o tipo de ingresso? (comum/estudante) "))
    total_a_pagar = 0
    for _ in range(quantidade):
        total_a_pagar += calcular_preco(tipo)

    if total_a_pagar > 0:
        print(f"Total a pagar: R${total_a_pagar}")
        confirmacao = input("Deseja confirmar sua compra? (sim/nao)")
        
        if confirmacao == "sim":
            ingressos_vendidos += quantidade
            
            print("Compra aprovada com sucesso!")
            
        else:
            print("Compra cancelada")
    
    else:
        print("Erro ao processar a compra.")
        
print("Todos os ingressos foram vendidos com sucesso! Obrigado")