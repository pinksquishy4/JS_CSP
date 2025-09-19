#JS old enough assignment

age = int(input("Please tell me your age:\n"))

if age >= 18:
    print("You are old enough to vote!")
elif age == 17 and age == 16:
    print("You are old enough to drive!")
elif age == 15:
    print("You are old enough to get a drivers permit.")
elif age >= 14:
    print("You are able to go to school")
else:
    print("You are too young to do anything fun!")