#Tip Calculator
print("Welcome to the tip calculator.")

#Receive user input
tot_bill = input("What was the total bill? ")
tip_perc = input("What percentage tip would you like to leave? ")
split_bill = input("How many people will split the bill? ")

#Calculate the tip
tip = float(tip_perc) / 100
tot_bill_float = float(tot_bill)
total_tip = tip * tot_bill_float
total_bill = round(total_tip + tot_bill_float, 2)
tot_split = total_bill / int(split_bill)
split_pay = round(tot_split, 2)
display_message = f"Your total bill after a {tip_perc}% tip is {total_bill}. Split by {split_bill} people, each person should pay {split_pay}"
print(display_message)