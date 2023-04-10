# Exercício 5.9 Escreva um programa que leia dois números. Imprima a divisão
# inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas
# os operadores de soma e subtração para calcular o resultado.

num_1 = int(input("Digite o primeiro numero:"))
num_2 = int(input("Digite o segundo numero:"))
x = 1 
quociente = 0
while num_2 <= num_1:
    if num_1 >= num_2:
        num_1 -= num_2
        quociente += 1  
resto = num_1
print(f"quociente {quociente}")
print(f"resto {resto}")