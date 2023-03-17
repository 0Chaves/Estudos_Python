#data types

#string
print("hello"[4])  #[] com um numero dentro servem para selecionar o indice da string, neste caso, o print vai mostrar O

#integer int
print(123 + 345)
print(100_000_000)

#float

3.1415

#boolean

True
False

#len() function nao funciona com int, apenas string

num_char = len(input("What's your name?\n"))
#print("Your name has " + num_char + " characters") da um erro, pois num_char é int e não da pra fazer concatenação de string com int

#print(type(num_char)) 
#a função type() permite mostrar qual o data type da variável

new_num_char = str(num_char) #str() converte o data type da variavel para string, mas ela precisa ser armazenada em uma nova variavel

print("Your name has " + new_num_char + " characters.")

a = str(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))
