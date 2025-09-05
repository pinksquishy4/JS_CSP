# JS 6th Expressions Notes

#What is an algorithm?
# A set of instructions to accomplish a task
#An expression is a list of numbers put together to create a solution
name = input("What is your name?")
print("Hello", name)

length = 5
width = 20
area = length * width
print(length,"+", width, "=", area)
#Algorithm for area

#List steps in an algorithm
#First, detirmine what pieces of information are needed (or variables)
# Second, proccess info
# Third, provide an output 
#1
age_one = 14
age_two = 14
age_three = 15
age_four = 15
#2
total= age_one + age_two + age_three + age_four
average = total/4 
#3
print("The average age between:", age_one, "-", age_two, "-", age_three, "-", age_four, "=", average)


#List ALL of the different mathematical operators (Give me the symbol and tell me what it does)
num_one = float(input("Give me a number:\n"))
num_two = int(input("Give me a number:\n"))
print("addition:", num_one + num_two)
print("Subtraction:", num_one - num_two)
print("Multiplication:", num_one * num_two)
print("division:", num_one / num_two)
print("exponents:", num_one ** num_two)
print("interger divison:", num_one // num_two)
print("modulo (remainder):", num_one % num_two)
#All you have to do for exponents is two stars, for addition the plus, for subtraction the minus, the division the slash, for interger divison, two slashes, and last modulo (remainder) is done with the percent sign %
# an Interger is a data type that can hold whole number
#a float is decimal number

#List ALL of the different assignment operators (Give me the symbols and what it does)
num_one += num_two
num_one -= num_two
print("addition (+):", num_one)
print("multiplication(*):", num_one)
print("division(/):", num_one)
print("subtraction(-)", num_one)
print("exponents(**):",num_one)
print("integer division(//):", num_one)
print("modulo(remainder)(%):", num_one)
#do this for the rest of the equations, you are just printing num_one over and over again.
#key word type in float and put parrenthsis around your input
num_one = float(input("Give me a number:\n"))
num_two = int(input("Give me a number:\n"))
#If you dont want a decimal do interger, if you do want it to have a decimal...do float
#Why are expressions so important in programming
#because if I set it up once, I never have to do it again.
