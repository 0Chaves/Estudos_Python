a = int(input("Primeiro número: "))
b = int(input("Segundo número: ")) 
c = int(input("Terceiro número: "))

if a > b and a > c:
    print("%d é o maior" % a)
if b > a and b > c:
    print("%d é o maior" % b)
if c > a and c > b:
    print("%d é o maior" % c)
if a < b and a < c:
    print("%d é o menor" % a)
if b < a and b < c:
    print("%d é o menor" % b)
if c < a and c < b:
    print("%d é o menor" % c)