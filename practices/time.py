# JS 6th Time of Day
import datetime
time = int(input("What time is it (military time)?\n"))

if time <= 11:
    print("Good morning!")
elif time <=17:
    print("Good Afternoon!")
elif time <=24:
    print("Good evening!")
else:
    print("That isnt even a time in day")