# JS Fincancial Calculator update

def clean(info):
    return float(input(f"what is your monthly {info}"))
def money(info, income):
    return info / income * 100
income = clean("income")
morgage = clean("rent/morgage")
utilities = clean("utilities")
groceries = clean("groceries")
transportation = clean("transportation")

savings = income * .1
total = income - (morgage + utilities + groceries + transportation + savings)

print(f"Your rent is $", morgage, "which is", money(morgage, income), "% of your income")
print(f"Your utilities are: $", utilities, "and that is", (utilities, income), "% of your income")
print(f"Your groceries are: $", groceries, "and that is", (groceries, income), "% of your income")
print(f"Your transportation is: $", transportation, "and that is", (transportation, income), "% of your income")
print(f"Your savings: $", savings, "and that is", income * .1, "% of your income")
print(f"You leftover money for spending is: $", total)