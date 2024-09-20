print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))

round_tip = round((bill * (tip) / 100),2)
bill_tip = bill + round_tip
print(bill_tip)
people = int(input("How many people to split the bill? "))
result = round((bill_tip / people),2)
print(f"Each person should pay: ${result}")