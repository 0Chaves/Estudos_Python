print("BMI - Body mass index calculator")
weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in m: "))
BMI = weight / height**2 


#------------------------------------------------

# print("BMI - Body mass index calculator")
# weight = input("enter your weight in kg: ")
# height = input("enter your height in m: ")

# BMI = float(weight) / float(height)**2 

# print("Your BMI is %.2f" % BMI)

#------------------------------------------------

if BMI < 18.5:
    print(f"Your bmi is {BMI}. You are underweight.")
elif BMI < 25:
    print(f"Your bmi is {BMI}. You have a normal weight.")
elif BMI < 30:
    print(f"Your bmi is {BMI}. You are overweight.")
elif BMI < 35:
    print(f"Your bmi is {BMI}. You are obese.")
else:
    print(f"Your bmi is {BMI}. You are clinically obese.")
