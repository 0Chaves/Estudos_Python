# Escreva um programa para calcular a redução do tempo de vida de
# um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos
# ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
# calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

cigarros_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos = int(input("Por quantos anos fumou: "))
cigarros_ano = 365*cigarros_dia
tempo_perdido = (cigarros_ano*10)/(24*60)
print("Você já perdeu %d dias de vida" % tempo_perdido)