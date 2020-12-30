"""
4 operações 1 hr

*funcao geral de operadores

exibir historico do resultado 30 min

apagar historico

"""
"""
import teste 
  
teste.soma_test()
teste.subtrair_test()
teste.dividir_test()
teste.mult_test()

"""

from operacoes  import * 

historico = []



while(True):

  resultado = 0
  

  print('("Digite sair para sair")')
  entrada = input("Digite 1 para soma, 2 para subtração, 3 para divisão, 4 para multiplicação")

  if entrada == 'sair':
    break
  else:
    entrada = int(entrada)
  



  if entrada == 1:
    valor1 = float( input("Digite o primeiro valor")  )
    valor2 = float( input("Digite o segundo valor")  )
    resultado = soma(valor1, valor2)
    print("O resultado da soma é, ", resultado)

  elif entrada == 2:
    resultado = subtract(float(input("Digite o primeiro valor")), float(input("Digite o segundo valor")))
    print("O resultado da subtração é, ", resultado)



  elif entrada == 3:
    valor1 = float( input("Digite o primeiro valor") )
    valor2 = float( input("Digite o segundo valor")  )
    resultado = division(valor1, valor2)
    print("O resultado da divisão é, ", resultado)


  elif entrada == 4:
    valor1= float(input("digite o primeiro valor"))
    valor2= float(input("digite o segundo valor"))
    resultado= mult(valor1,valor2)#a = valor1 -- b = valor2
    print ("O resutlado da multiplicação é,  ",resultado)
  else:
    print('Entrada incorreta')


  historico.append(resultado)

  print(historico)
  

