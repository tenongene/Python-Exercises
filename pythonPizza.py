# small = 15
# medium = 20
# large = 25
# pepp_sm = 2
# pepp_lg = 3
# cheese = 1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == 'S' or size == "s":
    bill += 15
elif size == 'M' or size == "m":
    bill += 20
elif size == 'L' or size == "l":
    bill += 25

if add_pepperoni == 'Y' or add_pepperoni == 'y':
    if size == 'S' or size == 's':
        bill += 2
    else:
        bill += 3
        
if extra_cheese == 'Y' or extra_cheese == 'y':
    bill += 1

print(f"Your total bill is ${bill}")
