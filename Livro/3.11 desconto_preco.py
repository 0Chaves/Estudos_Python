#Faça um programa que solicite o preço de uma mercadoria e o per-
#centual de desconto. Exiba o valor do desconto e o preço a pagar.

valor_produto = float(input("Preço do produto: "))
valor_desconto = float(input("Valor do desconto: "))
valor_final = valor_produto - valor_produto*valor_desconto/100
print("O preço final é R$%.2f com o desconto de %.2f por cento" % (valor_final, valor_desconto))