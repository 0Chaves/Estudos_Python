print("Calculadora de gorjeta")

#pede os valores ao usuario e define o tipo de dado
conta = float(input("Qual o valor total da conta?\n"))
gorjeta = int(input("A porcentagem da gorjeta será 10, 12 ou 15?\n"))
pessoas = int(input("Para quantas pessoas a conta será dividida?\n"))

#realiza os cálculos para o valor total da conta e o valor individual da conta
conta_total = conta + (conta*gorjeta/100) 
conta_individual = round((conta_total/pessoas),2)
a = "{:.2f}".format(conta_individual)

#exibe o valor individual a pagar
print(f"Cada pessoa deverá pagar {a}R$")