""" 
Laços infinitos (while) 

Exercício de fixação 6: Crie um programa que peça para o usuário inserir um login e uma senha. 
Caso os valores sejam iguais, informar que os dados são inválidos e pedir novamente as informações. 
Caso contrário, exibir a mensagem "Bem-vindo ao sistema!".
"""
while True:

    login = input("Login: ")
    senha = input("Senha: ")

    if login == senha:
        print("Dados Inválidos. Tente acessar novamente")
    
    else:
        print("Bem-Vindo ao sistema!")
        break # sair do loop quando as informações forem validas