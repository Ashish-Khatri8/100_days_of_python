# Day 2 project - Tip Calculator

# Greet the user.
print("Welcome to the Tip Calculator!")

# Prompt the user for bill amount.
bill_amount = float(input("How much is the bill?  $"))

# Ask what percentage of bill user would like to give as tip.
tip_percentage = float(input("What percentage of bill would you like to give as tip? "))

# Calculate the tip.
tip = (bill_amount * tip_percentage/100)

# Calculate the total bill.
total_bill_amount = bill_amount + tip

# Ask the user in how many people is the bill going to be split.
no_of_people = int(input("How many people are there to split the bill? "))

# Calculate overall bill for an individual and round it upto 2 decimal places.
individual_bill = round(total_bill_amount / no_of_people, 2)

# Print the output to the screen.
print(f"Each person has to pay : ${individual_bill}")
