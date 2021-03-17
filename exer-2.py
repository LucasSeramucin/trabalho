# 2 Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
N1 = float(input('Digite um numero: '))
if(N1 // 1 == N1):
    print('Numero inteiro!')
else:
    print("Numero decimal")