# Escreva um programa que pergunte a quantidade de km percorridos
# por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
# o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por
# dia e R$ 0,15 por km rodado.

km_percorrido = float(input("Digite a quantidade de quilômetros percorridos: "))
dias_alugado = int(input("Digite a quantidade de dias que foi alugado: "))
preco = km_percorrido*0.15 + dias_alugado*60
print("O valor a pagar é de R$%5.2f" % preco)