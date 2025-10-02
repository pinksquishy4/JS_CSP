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
#a bug is any error in my code that keeps it from running or makes it run improperly

#How do you debug the different types of errors?
#syntax error
#syntax error is like a grammar error in english class
#string = "This is my string' (this is a syntax error, because you wrote it wrong) Or if you forget an equal sign or a comma 


#Logic error
#its where our code does something that we dont expect it to do. this is a problem with the steps we took, too complete our process

#run time error
#when there is a problem in the code that will break the code when it is trying to run
#It wont pop up any syntex errors, but when we try to run it, it willl break.
#Describe what each of the methods below does:

#find()
print(sentance.find(brown))
print(sentance[10:15])
#So what this is doing is its going to my variable sentance and its going inside and its going to tell me where the word brown is located.
#concatenate (add)
first_name = input("What is your first name:\n").strip().title()
last_name = input("What is your last name:\n").strip().title()
full_name = first_name + " " + last_name
print
#upper()
#This will make all your lletter you put in uppercase
name = input("what is your name?:\n").strip().upper()
#lower()
#this will make all your letters you type in lowercase
name = input("What is your name?:\n").strip().lower()
#strip()
name = input("what is your name?:\n").strip()