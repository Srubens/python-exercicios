valorInvestido = float(input("Informe o valor investido "))
lucro = (valorInvestido * 20) / 100
total = valorInvestido + lucro
print("O Lucro do valor investido foi R${:.2f}".format(lucro), "dando um total de R${:.2f}".format(total))