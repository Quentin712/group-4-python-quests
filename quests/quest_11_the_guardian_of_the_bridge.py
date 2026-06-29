#This is to ask the user for there name
age = input ("Enter age:")
#This is to make sure the user inputs a number meaning if its anything other than a number it shows error
age = int (age)
#This check if the age is 18 or older and if the condition is true it prints the message below
if age >= 18:
    print("You are old enough to vote.")
