# Exercício 5.2 - Modifique o programa anterior para imprimir de 1 até o número
# digitado pelo usuário, mas, dessa vez, apenas os números ímpares.

x = 1
fim = int(input("Digite o ultimo numero impar a imprimir: "))
while x<=fim:
    if x%2 == 1:
        print(x)
    x+=1