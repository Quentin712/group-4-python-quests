#this quests , every adventurer has different name and quest.
#instead of using fixed values, we will use parameters, so the functions 
#can work with whatever data we will give it .
def personalized_greeting(name, quest):
    #name and quest are the parameters, they are acting as place holders.
    #and will be filled with what the user will input every time we call the function.
    print(f"{name}, your quest to {quest} has been recorded in the scrolls.")

#We will ask the user to input their info so the greeting is different every time.
#This is why parameters exist, to make functions more flexible and reusable.
user_name = input("What is your name? ")
user_quest = input("What is your quest? ")
#Then we will pass the user's answers into the functions as  arguments.
personalized_greeting(user_name, user_quest)
