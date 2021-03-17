# 3 Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.
N1 = int(input('Digite um numero: '))
N2 = int(input('Digite outro numero: '))
print('Qual operacao voce deseja realizar? ')
escolha = int(input('A:Adicao\nS:Subtracao\nM:Multiplicacao\nD:Divisao      :'     ))


if escolha == 1:
     print(N1 + N2)
elif escolha == 2:
    print(N1 - N2)
elif escolha == 3:
    print(N1 * N2)
elif escolha == 4:
    print(N1 / N2)

if (escolha%2)== 0:
    print('Numero e impar! ')
else:
    print('Numero e par!')
if(escolha // 1 == escolha):
    print('Numero e inteiro!')
else:
    print("Numero e decimal! ")
if(escolha > 0):
    print('O numero e positivo! ')
else:
    print('O numero e negativo! ')