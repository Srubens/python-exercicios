salarioA = float(input("Informe o valor do salario do trabalhador A: "))
salarioB = float(input("informe o valor do salario do trabalhador B: "))

if salarioA > salarioB :
    print("Salario A Maior R$ {:.2f}".format(salarioA))
else:
    print("Salario B Maior R$ {:.2f}".format(salarioB))