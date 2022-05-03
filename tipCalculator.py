bill = float(input("Welcome to the tip calculator.\nWhat is the total bill?\n"))
pct = float(input("What percentage tip would you like to give? (10%, 12%, 15% or 20%)\n"))
ppl = float(input("How many people would you like to split the bill?\n"))

tip = ((bill*(pct/100)) + bill)/ppl

print(f"Each person should pay: ${round(tip,2)}")