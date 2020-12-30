"""
PRECISO DE UM PROGRAMA QUE CALCULE O SALARIO MÉDIO DE 4 PESSOAS
"""

empresa = []

valorA = int(input("Digite o primeiro valor: \n"))
empresa.append(valorA)
valorB = int(input("Digite o segundo valor: \n"))
empresa.append(valorB)
valorC = int(input("Digite o terceniro valor: \n"))
empresa.append(valorC)
valorD = int(input("Digite o quarto valor: \n"))
empresa.append(valorD)

soma = sum(empresa)
retultado = soma / 4
print("O resultado obtido é: ",retultado)
print("O array da empresa é ",empresa)
print("A soma dos valores é ",soma)

