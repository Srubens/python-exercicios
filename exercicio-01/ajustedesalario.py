print("\nCargos da empresa: secretario, professor, coordenador, diretor, atendente")
cargo = input("Informe seu cargo:")


if cargo == "secretario":
    salario = float(1300)
    aumento = (float(salario * 10) / 100) + salario
    print("Secretario que ganha R${:.2f}".format(salario), " vai receber R${:.2f}".format(aumento))
elif cargo == "professor":
    salario = float(2200)
    aumento = (float(salario * 25) / 100) + salario
    print("Secretario que ganha R${:.2f}".format(salario), " vai receber R${:.2f}".format(aumento))
elif cargo == "coordenador":
    salario = float(3000)
    aumento = (float(salario * 11) / 100) + salario
    print("Secretario que ganha R${:.2f}".format(salario), " vai receber R${:.2f}".format(aumento))
elif cargo == "diretor":
    salario = float(4000)
    aumento = salario 
    print("Secretario que ganha R${:.2f}".format(salario), " vai receber R${:.2f}".format(aumento), "sem aumento")
elif cargo == "atendente":
    salario = float(1045)
    aumento = (float(salario * 15) / 100) + salario
    print("Secretario que ganha R${:.2f}".format(salario), " vai receber R${:.2f}".format(aumento))
else:
    print("Desculpe não temos este cargo aqui no momento! :(")
