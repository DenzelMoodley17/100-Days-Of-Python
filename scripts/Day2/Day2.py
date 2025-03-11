# Display welcome message

print("Welcome to the tip calculator?")

# Input value for the Tip Calculator program.

bill_total = float(input("What was the total bill? $ "))
tip_percent = int(input("How much tip would you like to give? 10, 12, 15? "))
people = int(input("How many people to split the bill? "))

total_pay = (bill_total * (tip_percent / int(100))) + bill_total
split_pay = round(total_pay / people)

print(split_pay)
