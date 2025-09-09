#JS 6th string notes
print("I did it!")

#What makes something a string?
#a string is just a collection of symbols held together by quotaion marks. Types of quoataions dont matter as long as they are matching. "content of string", 'this is also a string'. 
#Every input has a string assoicated with it
#Examples of strings
name = input("what is your name?:\n").strip().upper() 
name = input("What is your name?:\n").strip().lower()
name = input("What is your name?:\n").strip().capitalize()
name = input("What is your name?:\n").strip().title()
#this is going to get rid of any extra spaces the user puts in
sentance = "The quick brown fox jumps over the lazy dog."
print("Welcome to my program", name)
#Why do we have strings?
#Strings are the only data type that allows us to use letters. 

#How do stupid proofing and sanitization relate to each other?

#What is debugging?
#Debugging is fixing problems in my code

#How do you debug the different types of errors?
#syntax error
#Logic error
#run time error
#Describe what each of the methods below does:

#find()

#concatenate (add)
first_name = input("What is your first name:\n").strip().title()
last_name = input("What is your last name:\n").strip().title()
full_name = first_name + " " + last_name
print
#upper()
name = input("what is your name?:\n").strip().upper()
#lower()
name = input("What is your name?:\n").strip().lower()
#strip()
name = input("what is your name?:\n").strip()