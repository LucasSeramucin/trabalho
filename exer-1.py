# 1: Faça um Programa que peça um número
# inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisao)
N1 = int(input('Digite um numero inteiro: '))
if(N1%2) == 0:
    print('O numero digitado é Par')
else:
    print('O numero digitado é Impar')