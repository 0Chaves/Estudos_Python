#Faça um programa que calcule o aumento de um salário. Ele deve 
#solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

print("Cálculo de aumento do salário")
salario = float(input("Digite o valor do salário: "))
aumento = float(input("Digite o valor do aumento: "))
final = salario + salario*aumento/100
print("O novo salário é R$%.2f com o aumento de %.2f por cento" % (final, aumento))

