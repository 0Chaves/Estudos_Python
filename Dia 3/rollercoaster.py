print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 130:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print(f"Child tickets are {bill}$.")
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are {bill}$.")
    elif age >= 45 and age <= 55:
        bill = 0
        print(f"Mid age tickets are free.")
    else:
        bill = 12
        print(f"Adult tickets are {bill}$.")

    wants_photo = input("Do you want a photo taken? y or n ")
    if wants_photo == "y":
        #add 3 to their bill
        bill += 3

    print(f"Your final bill is {bill}$")
    

else:
    print("Sorry, you have to grow taller before you can ride.")
