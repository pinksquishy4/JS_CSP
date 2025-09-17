# JS 6th Conditionals notes

#What puts something inside of the “if” statement?
#the base piece of a conditional
num = 12

if num < 10:
    print(f"{num} is a single digit number")
elif num < 100:
    print(f"{num} is a two digit number")

#What do if statements do?
#our keyword if is telling the computer to check a true or false statement

#What are boolean statements? 
#its something that will be true or false "num < 10"

#What do else statements do?
#else statemnt and it is what a conditional should always end in
#They catch everything else that is left over a "catch all"
#else:
    #print(f"{num} is not a single digit number")


#What kind of statement do you use if you have more than 2 needed outcomes?
#You use elif
name = input("Please tell me your name")

if name == "Ms LaRose":
    print("You are the teacher!")
elif name == "Tia":
    print("You are the TA!")
else:
    print(f"hello {name}, you are a student")

#What do each of the different symbols mean in conditionals?
#These are comparison operators
#<
#less than symbol
#>
#Greater than symbol
#<=
#less than or equal to
#>=
#greater than or equal to
#==
#to see if its equal or else it will think we are setting a variable
#!
#to see if its not equal to

#What are the 3 logical operators?

#What are logical operators for?

#What does a nested conditional statement do?
