#Exercício 5.3 Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.

x = 3
mult = 1
inicio = 1
fim = int(input("Digite quantos multiplos de 3 serão mostrados: "))
while inicio <= fim:
    print(x*mult)
    mult += 1
    inicio += 1