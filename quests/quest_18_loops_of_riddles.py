#In this quest, the user tries to guess the number until he gets it right.
# So, we want to keep repeating an action until the user provide the correct input
#We need to generate random numbers
import random 
#This command lets you generate random number, selections or shuffle items.
secret_number = random.randint(1,100)
#random.randint picks a random number from 1-100 
guess = None 
#We use while-loop as we need to keep asking the user to guess until the number is true 
while guess != secret_number:
    #!= means not equal 
    guess = int(input("Guess a number from 1-100: "))
    if guess != secret_number:
        print("Wrong, try again")
    #Here, if user's guess is not equal to the secret_number then it will continue asking him to guess until he gets it right 
print("You got it right")
#Here if the user guess it right, the above message will appear 

