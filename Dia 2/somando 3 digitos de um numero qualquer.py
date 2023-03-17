#Criar um programa que, ao colocar um numero aleatório de 3 digitos, ele envia a soma dos digitos

#Pede o número ao usuário e converte para string
num = input("Digite um número de 3 digitos: ")    #input já traz o resultado como string, mesmo que seja digitado apenas numeros

#Converte cada índice da string em int
a = int(num[0])
b = int(num[1])
c = int(num[2])

#Mostra a soma dos algarismos
print(a + b + c)



#------------------------------------------

