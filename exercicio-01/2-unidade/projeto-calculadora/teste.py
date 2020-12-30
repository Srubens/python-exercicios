
from operacoes import soma, subtract, mult, division 



#---------- Teste
def soma_test():
  
  resultado = soma(3, 2)
  if type(resultado) == type(1):
    print('Tipo de dado do retorno de soma correto')

  else:
    print('Tipo de dado do retorno de soma incorreto')




  if resultado == 5:
    print('Funcionalidade de somar tá correta')
  else:
    print('Funcionalidade de somar tá incorreta')


def subtrair_test():
  resultado = subtract(3, 2)
  if resultado == 1:
    print('Funcionalidade de subtrair tá correta')
  else:
    print('Funcionalidade de subtrair tá incorreta')

def mult_test():
  resultado = mult(3, 2)
  if resultado == 6:
    print('Funcionalidade de mult tá correta')
  else:
    print('Funcionalidade de mult tá incorreta')

def dividir_test():
  resultado = division(4, 2)
  if resultado == 2:
    print('Funcionalidade de div tá correta')
  else:
    print('Funcionalidade de div tá incorreta')