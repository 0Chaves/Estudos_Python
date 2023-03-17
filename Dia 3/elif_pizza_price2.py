print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L : ") #Small:$15 , Medium:$20 , Large:$25
add_pepperoni = input("Do you want pepperoni? Y or N : ") #pepperoni for small:+$2 , for medium or large:+$3
extra_chesse = input("Do you want extra chesse? Y or N :") #extra chesse for any:+$1

price = 0

#Set pizza price by size
if size == "S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25

# check if they added pepperoni
if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

#Check if they added extra chesse
if extra_chesse == "Y":
    price += 1

print(f"The price of the pizza is: ${price}")