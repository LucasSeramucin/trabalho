# 4-Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
print('Responda todas as perguntas com "1 para sim ou 0 para Nao." ')
P1 = int(input('Telefonou para a vitima?:1/Sim ou 0/Nao:'))
P2 = int(input('Esteve no local do crime?:1/Sim ou 0/Nao: '))
P3 = int(input('Mora perto da vitima?:1/Sim ou 0/Nao: '))
P4 = int(input('Devia para a vitima?:1/Sim ou 0/Nao: '))
P5 = int(input('Ja trabalhou com a vitima?:1/Sim ou 0/Nao: '))
Resultado = P1 + P2 + P3 + P4 + P5
if (Resultado<2):
    print('Inocente')
elif (Resultado == 2):
    print('Suspeito')
elif (3<= Resultado <= 4):
    print('Cumplice')
elif (Resultado == 5):
    print('Assassino')