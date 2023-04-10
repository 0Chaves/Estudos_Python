# Exercício 5.8 Escreva um programa que leia dois números. Imprima o resultado da
# multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e
# subtração para calcular o resultado.

num_1 = int(input("Digite o primeiro numero:"))
num_2 = int(input("Digite o segundo numero:"))
resultado = 0
x = 1
while x<=num_2: 
    resultado += num_1
    x += 1
print(resultado)