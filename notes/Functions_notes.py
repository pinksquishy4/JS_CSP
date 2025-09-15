#JS 6th functions notes
import random
#What a function is
#Just a set of instructions that are excuted when you have a key word
#print is a function, input is a function
#Why we use functions
#you put things in a function so you dont have to rewrite it over and over again
name = input("what is your name?\n")
print(f"hello {name}!")
#How to write a function in Python
def welcome ():
    name = input("what is your name")
    print(f"hello {name}!")

print(f"the function is over!")
welcome()
welcome()
welcome()
welcome()
welcome()
#you have to have the dents match exactly or it will break
#If you call welcome before you define it, it wont know what to do
#use keyword def, then give it a name, then parenthesis then colon

#What parameters and arguments are
#if you want to change the variables, youj wll
#parameters go inside the paranethesis when you define your function
#Argument are given when we call the function
#code that is prebuilt to give a specific action

#How to use parameters and arguments in python
def add(number):
    number = number + num_two
    print (number)
num_one = 12
num_two = 14
#add(num_one, num_two)
#add(9, 700)
#add(4, 8)
#add(87, 45)
#Varibles are used when i want to do the same thing over
#What return statements are
#Its going to take what is inside your function and place it wxactly where your function is calleed
def clean(info):
    info.strip().lower()

name = input("what is your name?\n")
quest = input("what is your quest?\n")
color = input("What is your favorite color")
print(f"Hello, {clean(name)} I have heard you are trying to {clean(quest)}, That is super cool! ar you sure {clean(color)} is your favorite color?"  )

def believe(sentance):
    length = len(sentance)
    spot_one = random.randint(0, length -1)
    spot_two = random.randint(0, length -1)
    spot_three = random.randint(0, length -1)
    full_sentence = sentance.split()
    full_sentence.insert(spot_one, "Believe it!")
    #something like this
    #At the end put return sentence