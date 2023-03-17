#Escreva um programa que calcule o tempo de uma viagem de carro.
#Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

dist = float(input("Qual a distancia do trageto: "))
vel_med = float(input("Qual a velocidade media estimada: "))
tempo = dist/vel_med 
print("O tempo estimado para a viagem é de %.0f horas" % tempo)