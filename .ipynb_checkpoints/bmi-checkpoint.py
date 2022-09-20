weight = float(input("What is your weight in kg?  "))
height = float(input("What is your height in meters?  "))

bmi = weight/(height**2)

print(f"Your BMI is {round(bmi,2)}")