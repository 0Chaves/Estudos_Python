operacao = input("Qual operação deseja fazer?\n+ para soma\n- para subtração\n/ para divisão\n* para multiplicação\n")
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "/":
    resultado = round(num1 / num2 , 2)
else:
    operacao = num1 * num2

print("%.2f" % resultado)