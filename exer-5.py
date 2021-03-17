combustivel = str(input("Digite o tipo de combustível que você colocou:")).strip().capitalize()
Litros = float(input('Quantos litros foi colocado? '))
if combustivel == "A":
    alcool = 1.9
    custo = Litros * alcool

if Litros <= 20:
    alcool = 1.9
    custo = Litros * alcool
    desconto1 = (custo * 3)/100
    print(f"O desconto do alcool foi de  {desconto1} e o preço agora o preco e de {custo-desconto1}")

elif Litros > 20:
    alcool = 1.9
    custo = Litros * alcool
    desconto2 = (custo * 5) / 100
    print(f'O desconto do alcool foi de {desconto2}, o preco agora o preco e de {custo-desconto2}')

elif combustivel == "G":
    gasolina = 2.5
    custo = Litros * gasolina

if Litros <= 20:
    gasolina = 2.5
    custo = Litros * gasolina
    Desconto3 = (custo*4)/100
    print(f'O desconto do preco da gasolina foi de {Desconto3}, agora o preco e de {custo - Desconto3}')
elif Litros > 20:
    custo = Litros * gasolina
    desconto4 = (custo*6)/100
    print(f'O desconto do preco da gasolina foi de {desconto4}, agora e de {custo-desconto4}')

