print("Calculadora de gorjeta")

#pede os valores ao usuario e define o tipo de dado
conta = float(input("Qual o valor total da conta?\n"))
gorjeta = int(input("A porcentagem da gorjeta será 10, 12 ou 15?\n"))
pessoas = int(input("Para quantas pessoas a conta será dividida?\n"))

#realiza os cálculos para o valor total da conta e o valor individual da conta
conta_total = conta + (conta*gorjeta/100) 
conta_individual = conta_total/pessoas

#exibe o valor individual a pagar
print(f"Cada pessoa deverá pagar {round(conta_individual)}R$")