# PROGRAMA QUE RETORNA O IMC

peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))
imc = peso / (altura ** 2)

# print(imc)

if imc > 39.9:
    print("Obesidade grave Gordo pra C$R4LHO {:.2f}".format(imc))
elif imc <= 39.9 and imc >= 30:
    print("Obesidade Gordo! {:.2f}".format(imc))
elif imc <= 29.9 and imc >= 25:
    print("Sobrepeso {:.2f}".format(imc))
elif imc >= 18.5 and imc <= 24.9:
    print("Peso ideal  {:.2f}".format(imc))
else:
    print("Magreza!! {:.2f}".format(imc))

