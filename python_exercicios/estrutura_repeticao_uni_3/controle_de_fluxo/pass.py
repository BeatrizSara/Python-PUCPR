"""  
Exemplo comando PASS
O comando pass não faz nada. É usado quando a sintaxe exige um bloco de código, 
mas você não quer executar nada dentro desse bloco.
"""
for i in range(10):
    if i % 2 ==  0:
        pass
    else:
        print(i)
        
#Esses comandos são úteis para controlar o comportamento de loops em situações específicas, 
# como interromper um loop prematuramente, pular iterações ou indicar blocos vazios de código.