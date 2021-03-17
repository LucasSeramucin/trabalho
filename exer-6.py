# 6-Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá
# ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos
# e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
MorangoKg = float(input('Quantos kilos de morango voce pegou?: '))
MacaKg = float(input('Quantos kilos de maca voce pegou?: '))
if MorangoKg > 5:
    Morangovalor = 2.2

elif MorangoKg <=5:
    Morangovalor = 2.5
if MacaKg > 5:
    Macavalor = 1.5
elif MacaKg <= 5:
    Macavalor = 1.8

ValorF = (Macavalor*MacaKg) + (Morangovalor*Morangovalor)
descontoT = (ValorF*10)/100


if ValorF > 25:
    print(str(f'o seu desconto foi de {descontoT} logo seu preco final e {ValorF-descontoT}.'))
elif ValorF <= 25:
    print(str(f'O valor de sua compra foi de :{ValorF}.'))