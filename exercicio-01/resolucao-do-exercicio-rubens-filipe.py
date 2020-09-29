"""
1 - Escreva um programa que converta a temperatura de Fahrenheit para celsius;
"""

fahrenheit = float(input("Informe a temperatura: "))
celsius = (fahrenheit - 32) / 1.8
print("O valor de Celsius é {:.2f}".format(celsius))

"""
2 - Escreva um programa que solicite o ano de nascimento e calcule a idade atual;
"""
nascimento = int(input("Informe o ano do seu nascimento: "))
anoAtual = 2020 - nascimento
print("Você tem", anoAtual, "anos.")

"""
Escreva um programa que calcule o saldo de investimento após descontar 20%
do rendimento
"""
# valorInvestido = float(input("Informe o valor investido "))
# lucro = (valorInvestido * 10) / 100 + valorInvestido
# descontoVinte = (valorInvestido * 20) / 100
# total = lucro - descontoVinte
# print("O valor investido foi de R${:.2f}".format(valorInvestido), "o desconto do ivestimento -20% R${:.2f}".format(descontoVinte), 
# "teve um rendimento de R${:.2f}".format(lucro),"dando um total de R${:.2f}".format(total))

"""
Escreva um programa para calcular a conta de telefone seguindo as intruções:
Abaixo de 200 minutos, a empresa cobrea R$0,20 por minuto. 
Entre 200 e 400, o preço é R$ 0,18. Acima de 400 minutos o preço por minuto é R$ 0,15.
"""
# conta = float(input("Informe quantos minutos você ficou ao telefone: "))

total = conta
if total <= 199:
    total *= 0.2
    print("Você ficou {:.2f}".format(total), " minutos no telefone. Dando um total de R${:.2f}".format(total))
elif total >= 200 and total <= 399:
    total *= 0.18
    print("Você ficou {:.2f}".format(total),
          " minutos no telefone. Dando um total de R${:.2f}".format(total))
else:
    total *= 0.15
    print("Você ficou {:.2f}".format(total),
          " minutos no telefone. Dando um total de R${:.2f}".format(total))


"""
Escreva um programa de ajuste de salario de acorto com a tabela abaixo:

 ----------------------------------
|codigo | cargo | aumento          |
|----------------------------------|
|1      | secretario  |  10%       |
|2      | professor   |  25%       |
|3      | coordenador |  11%       |
|4      | diretor     |sem aumento |
|5      | atendente   |  15%       | 
-----------------------------------
"""

# print("\nCargos da empresa: secretario, professor, coordenador, diretor, atendente")
# cargo = input("Informe seu cargo:")


if cargo == "secretario":
    salario = float(1300)
    aumento = (float(salario * 10) / 100) + salario
    print("Secretario que ganha R${:.2f}".format(
        salario), " vai receber R${:.2f}".format(aumento))
elif cargo == "professor":
    salario = float(2200)
    aumento = (float(salario * 25) / 100) + salario
    print("Secretario que ganha R${:.2f}".format(
        salario), " vai receber R${:.2f}".format(aumento))
elif cargo == "coordenador":
    salario = float(3000)
    aumento = (float(salario * 11) / 100) + salario
    print("Secretario que ganha R${:.2f}".format(
        salario), " vai receber R${:.2f}".format(aumento))
elif cargo == "diretor":
    salario = float(4000)
    aumento = salario
    print("Secretario que ganha R${:.2f}".format(
        salario), " vai receber R${:.2f}".format(aumento), "sem aumento")
elif cargo == "atendente":
    salario = float(1045)
    aumento = (float(salario * 15) / 100) + salario
    print("Secretario que ganha R${:.2f}".format(
        salario), " vai receber R${:.2f}".format(aumento))
else:
    print("Desculpe não temos este cargo aqui no momento! :(")


"""
6 - Faça um programa que le uma quantidade de valores e calcula a media e a soma
"""
#FIZ EM JAVASCRIPT NAO CONSEGUIR COLOCAR EM PYTHON

