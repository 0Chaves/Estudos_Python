# Escreva um programa que converta uma temperatura digitada em °C em °F.

print("Conversor de temperatura - °C para °F ")
temp_c = int(input("Coloque a temperatura em celcius: "))
temp_f = 9*temp_c/5+32
print("%d°C equivalem a %d°F" % (temp_c, temp_f))