"""
1- Escreva um programa que solicite o nome sobrenome e retorne bem vindo 
"""
# nome = input("Digite seu nome: \n")
# sobrenome = input("Digite seu sobrenome: \n")
# print("Bem vindo", nome, sobrenome)

"""
2- Escreva um programa que solicite um numero e retorna se é impa ou par 
"""
# numero = int(input("Digite um numero: \n"))
# if numero % 2 == 0:
#     print("o numero é", numero, "ele é par")
# else:
#     print("o numero é", numero, "ele é impar")

"""
3- Escreva um programa que solicite nome, idade e se é um usuario premium
"""
# nome = input("Digite seu nome: \n")
# idade = input("Digite sua idade: \n")
# userPremium = str(input("Você é um usuario premium?\nSe sim Digite sim, do contrario digite nao\n"))
# if userPremium == "sim":
#     print("O usuario", nome, "tem", idade, "ele é um usuario premium")
# else:
#     print("O usuario", nome, "tem", idade, "não é um usuario premium")


"""
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo,
sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração
mínima de 1 hora e máxima de 24 horas.
"""

# hInicial = str(input("Digete o horario inicial que o jogador começou o jogo\nSendo de 1 à 24:\n"))
# mInicial = str(input("Digite o minuto incial que o jogador começou o jogo\nSendo 00 à 59\n"))
# hFinal = str(input("Digete o horario inicial que o jogador finalizou o jogo\nSendo de 1 à 24:\n"))
# mFinal = str(input("Digite o minuto incial que o jogador finalizou o jogo\nSendo 00 à 59\n"))
# horasJogadas = int(int(hFinal)+int(mFinal) - int(hInicial)+int(mInicial))

# hInicial = float(input("Digete o horario inicial que o jogador começou o jogo\n"))
# hFinal = float(input("Digete o horario final que o jogador começou o jogo\n"))

# def myHorario(horario):
#     if horario == 1.59:
#         return round(2)
#     elif horario == 2.59:
#         return round(3)
#     elif horario == 3.59:
#         return round(4)
#     elif horario == 4.59:
#         return round(5)
#     elif horario == 5.59:
#         return round(6)
#     elif horario == 6.59:
#         return round(7)
#     elif horario == 7.59:
#         return round(8)
#     elif horario == 8.59:
#         return round(9)
#     elif horario == 9.59:
#         return round(10)
#     elif horario == 10.59:
#         return round(11)
#     elif horario == 11.59:
#         return round(12)
#     elif horario == 12.59:
#         return round(13)
#     elif horario == 13.59:
#         return round(14)
#     elif horario == 14.59:
#         return round(15)
#     elif horario == 15.59:
#         return round(16)
#     elif horario == 16.59:
#         return round(17)
#     elif horario == 17.59:
#         return round(18)
#     elif horario == 18.59:
#         return round(19)
#     elif horario == 19.59:
#         return round(20)
#     elif horario == 20.59:
#         return round(21)
#     elif horario == 21.59:
#         return round(22)
#     elif horario == 22.59:
#         return round(23)
#     elif horario == 23.59:
#         return round(24)
#     else:
#         return horario


# if myHorario(hFinal) > myHorario(hInicial):
#     horaTotal = myHorario(hFinal) - myHorario(hInicial)
#     # print(horaTotal)
# elif myHorario(hInicial) > myHorario(hFinal):
#     horaTotal = myHorario(hInicial) - myHorario(hFinal)
#     # print(horaTotal)

# print("O jogador ficou jogando {:.2f}".format(horaTotal), "horas")
# print("Horario inicial ", myHorario(hInicial))
# print("Horario inicial ", myHorario(hFinal))

# hInicial = int(input("Digete o horario inicial que o jogador começou o jogo \n"))

# hFinal = int(input("Digete o horario final que o jogador começou o jogo \n"))


# hTotal = hFinal - hInicial 
# print(hTotal)

# print("O jogador ficou", hTotal, "horas")

"""
Escreva um programa que solicita o nome, o email e retorna se o login foi realizado com
sucesso
"""
# nome = str(input("Digite seu nome: \n"))
# email = str(input("Digite seu e-mail: \n"))
# checkNome = nome
# checkEmail = email
# print(checkNome, checkEmail)
# if nome == checkNome and email == checkEmail:
#     print("Login realizado com sucesso!")

"""
Escreva um programa calculadora do AND utilizando 0 e 1 
"""
# valorA = int(input("Digite um valorA: \n"))
# valorB = int(input("Digite um valorB: \n"))
# valorC = int(input("Digite um valorC: \n"))
# valorD = int(input("Digite um valorD: \n"))

# if valorA > valorB and valorC > valorD:
#     print("Verdadeiro", 0)
# else:
#     print("Falso", 1)

"""
Escreva um programa calculadora do OR utilizando 0 e 1
"""

# valorA = int(input("Digite um valorA: \n"))
# valorB = int(input("Digite um valorB: \n"))
# valorC = int(input("Digite um valorC: \n"))
# valorD = int(input("Digite um valorD: \n"))

# if valorA > valorB or valorC > valorD:
#     print("Verdadeiro", 0)
# else:
#     print("Falso", 1)

"""
Escreva um programa que solicita as duas notas, calcula a média, e retorna a seguinte
mensagem com base na média:
Nota abaixo de 4: Você precisa estudar mais
Nota entre 4 e abaixo de 7: Você vai ter outra chance
Nota entre 7 e 9: Parabens vc foi aprovado
Nota acima de 9: Parabens, vc obteve uma nota excelente
"""

# notaA = float(input("Digite a nota 1: \n"))
# notaB = float(input("Digite a nota 2: \n"))
# media = (notaA + notaB) / 2
# if media < 4:
#     print("Você precisa estudar mais")
# elif media >= 4 and media <= 6.9:
#     print("Você vai ter outra chance")
# elif media >= 7 and media <= 9:
#     print("Parabens vc foi aprovado")
# else:
#     print("Parabens, vc obteve uma nota excelente")

# print("Sua nota foi ", media )

"""
Escreva um programa que diga qual o grupo de usuario de acordo com a idade e o
gênero:
- bebê <= 1
-- criança > 1 e menor de 12
--jovem > 12 e menor 18
-- jovem de maior >= 18 e menor 25
-- adulto > 25 e menor de 60
--- maior de 60 é idoso
"""
# pessoaIdade = int(input("Digite a sua idade:\n"))

# if pessoaIdade <= 1:
#     print("bebê")
# elif pessoaIdade > 1 and pessoaIdade < 12:
#     print("infantil")
# elif pessoaIdade >= 12 and pessoaIdade < 18:
#     print("adolescente")
# elif pessoaIdade >= 18 and pessoaIdade < 25:
#     print("Jovem")
# elif pessoaIdade >= 25 and pessoaIdade < 60:
#     print("adulto")
# else:
#     print("idoso")

"""
- -----Escreva um programa que leia um valor qualquer e apresente uma mensagem dizendo
em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra.
Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a
mensagem “Fora de intervalo”.
O símbolo ( representa "maior que". Por exemplo: [0,25] indica valores entre 0 e 25.0000,
inclusive eles. (25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.00
"""
valor = int(input("Digite um valor de 0 à 100: \n"))
if valor >= 0 and valor < 25:
    print("o valor esta entre 0 e 25 \n",valor)
elif valor >= 25 and valor < 50:
    print("o valor esta entre 25 e 50 \n",valor)
elif valor >= 50 and valor < 75:
    print("o valor esta entre 50 e 75 \n",valor)
elif valor >= 75 and valor < 100:
    print("o valor esta entre 75 e 100 \n", valor)
else:
    print("fora do intervalo!")
