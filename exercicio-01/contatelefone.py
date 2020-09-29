conta = float(input("Informe quantos minutos você ficou ao telefone: "))
dias = float(input("Quantos dias você fez ligações? "))

total = conta * dias
if total <= 199:
    total *= 0.2
    print("Você ligou ", dias, "dias e ficou ",conta, " minutos no telefone. Dando um total de R${:.2f}".format(total))
elif total >= 200 and total <= 399:
    total *= 0.18
    print("Você ligou ", dias, "dias e ficou ",conta, " minutos no telefone. Dando um total de R${:.2f}".format(total))
else:
    total *= 0.15
    print("Você ligou ", dias, "dias e ficou ",conta, " minutos no telefone. Dando um total de R${:.2f}".format(total))