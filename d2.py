#Tip Calculator
print("Welcome to the tip calculator")
total = float(input("What was the total bill?"))
people = float(input("How many people to split the bill?"))
percentage = float(input("What percentage tip would you like to give?"))
tip = ((percentage/100) * total) + total
print("Each person should pay: ", tip)
