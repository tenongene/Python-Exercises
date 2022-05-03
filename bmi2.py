name = input("What is the person's name?\n")
weight = float(input("What is the weight in kg?  "))
height = float(input("What is the height in meters?  "))

bmi = round(weight/(height**2), 2)

# print(f"Your BMI is {bmi}")

if bmi < 18.5:
    print(f"{name}'s BMI is {bmi} and is underweight")
elif bmi > 18.5 and bmi < 25:
    print(f"{name}'s BMI is {bmi} and has a normal weight")
elif bmi > 25 and bmi < 30:
    print(f"{name}'s BMI is {bmi} and is overweight")
elif bmi > 30 and bmi < 35:
    print(f"{name}'s BMI is {bmi} and is obese")
else:
    print(f"{name}'s BMI is {bmi} and is clinically obese") 