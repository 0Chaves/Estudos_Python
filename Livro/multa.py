velocidade = int(input("Com qual velocidade cruzou o radar?\n"))
multa = 0

if velocidade > 80:
    multa = (velocidade-80)*5
    print(f"Você foi multado em {multa}R$.")
