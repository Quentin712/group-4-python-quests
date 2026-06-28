def ask_for_age():
    #this function asks the user to input their age so it can be passed to the next function
    age = int(input("How old are you? "))
    return age

def can_they_vote(age):
    #This function already received the age that was returned from ask_for_age().
    #It then decides to display whether the user can vote or not yet.
    if age >= 18:
        print("You can vote.")
    else:
        print("Not Yet, Give it a few years.")

#ask_for_age() runs first and then will return the age into the user_age.
#Then we pass user_age into can_they_vote() to make the final decision.
user_age = ask_for_age()
can_they_vote(user_age)
