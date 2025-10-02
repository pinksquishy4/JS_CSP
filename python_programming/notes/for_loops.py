# JS 6th Time and For Loops notes
import datetime


current = datetime.datetime.now()
hour = current.hour
print(f"The time is: {current}")
print(f"The hour is: {hour}")


#What is a loop?
 #its going to kee[ going until a specific condition is met]
#What are the two types of loops?
#for loops, while loops

# for each student, in the row marker got passes down
#What is iteration
# 1 itetrator (keep track of loop#)
#ONE instance of a loop, we iterate by looping something over and over again, our iteration is that peticular instance of a loop.

#What are lists?
  #it allows you to store multiple pieces of information within the same variable
#How do you make lists in python?
siblings = ["Alexxis", "Isabelle", "Danielle", "Zane", "Nicole", "Juliette", "Kylie", "Valerie", "Anthony", "Bella", 8, 3.1459 ]
#This is a list of strings, but you can have a list of intergers or any data type, including other lists/
#It can have any information, it just has to be seprated by commas
print(siblings[5])
siblings[6] = "Kylie"
siblings[7] = "valerie"
siblings.remove("Juliette")
#for loop


#How do you make for loops in python? 
for sibling in siblings: 
    print(f"Hello {sibling}")
for x in range (20, 0, -1): #You have to go one less than what you want it to go, if you want it to go to 1, write 0
    print(x)  
#How do you make while loops in python?
#They are like for loops, but they are more likely to create a bug in your code, an infinite loop

#This one is in infinite while loop

#while True:
  #  print("oh NO!")

#1. iterator (keep track of loop#)
#2. end condition (tells the loop to stop)
#3. increase the iterator
# Good while loop
i = 1

while i < 21:
    if i % 2 == 0: #useful equation, if i divided by 2 has a remainder of 0, then it will be even
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
    i += 1 #this increases our i variable by one

import random

number = random.randint(1,20)
x = 1
#while x != number:
   # print("Duck")
  #  x += 1
#print("Goose!")

while True:
    if number == x:
        print("Goose!")
        break #this statement breaks the loop
    else:
        print("Duck")
        x += 1

 