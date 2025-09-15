#JS 6th financial calculator

income = float(input("Hello, what is your monthly income?:"))
rent = float(input("What is your monthly rent/mortgage?:"))
utilities = float(input("what is your monthly utilites cost?:"))
groceries = float(input("What is the monthly cost of groceries?:"))
transporation = float(input("What is the monthly cost of your transportation?:"))

spending_money = float(income - (rent + utilities + groceries + transporation))
total_expenses = float(income + rent + utilities + groceries + transporation)

rent_pct = float(rent / income) * 100
utilities_pct = float(utilities / income) * 100
groceries_pct = float(groceries / income) * 100
transporation_pct = float(transporation / income) * 100
savings = float(income *0.10)
savings_pct = 10

print("Your rent is $", rent, "and that is", rent_pct, "%, of your income.")
print("Your utilities are $", utilities, "and that is", utilities_pct, "%, of your income.")
print("Your groceries are $", groceries, "and that is", groceries_pct, "%, of your income.")
print("Your transportation is $", transporation, "and that is", transporation_pct, "%, of your income.")
print("you should save", savings, " a month, and that is", savings_pct, "%, of your income.")
print("You should have", spending_money, " of money left over for spending.")



