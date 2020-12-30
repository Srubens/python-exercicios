
"""
Faça um programa que cadastra mais de um usuário e a respectiva senha. Depois permita que o usuário possa realizar o login.

"""
controle = True


userNome = input("Insira seu nome: \n")
userSenha = input("Insira seu senha: \n")
arrUser = []
arrUser.append(userNome)
arrUser.append(userSenha)

valorNome = input("Seu nome: \n")
valorSenha = input("Sua senha \n")
arrValor = []
arrValor.append(valorNome)
arrValor.append(valorSenha)

if arrUser == arrValor:
    print("Ola %c bem vindo!", arrUser[0])
else:
    print("Erro login ou usuario")
