#PROGRAMA QUANTO GANHO POR DIA

# ganhoPH = int(input("Quanto você ganha por hora? "))
# numeroH = int(input("Numero de horas trabalhadas no mês? "))
# valor = (ganhoPH * numeroH)
# print("Você ganha R$", valor)

salario = float(input("Informe o valor do seu salario: "))
horasTrabalho = float(input("Informe quantas horas de trabalho: "))
salarioMes = salario / 30
valorHora = salarioMes / horasTrabalho
print("Seu valor hora é R$ {:.2f}".format(valorHora))
