idade = int(input ("Qual a sua idade?\n"))
#unidades fixas
idade_max = 90 #considerando uma vida que dure 90 anos
meses_ano = 12
semanas_ano = 52
dias_ano = 365
#calculos de tempo restante
meses_restantes =  (idade_max*meses_ano) - (idade*meses_ano)
semanas_restantes = (idade_max*semanas_ano) - (idade*semanas_ano)
dias_restantes = (idade_max*dias_ano) - (idade*dias_ano)

#Mostra o resultado
print(f"Você possui {meses_restantes} meses; {semanas_restantes} semanas; {dias_restantes} dias restantes até seus 90 anos")

