#Asks user to choose their direction
direction = input("GO 'LEFT' or 'RIGHT'? ")
direction = direction.upper()

#Check the direction choosen
if direction == "LEFT":
    #This is brought only if user chose left
    action = input ("Want to 'SWIM' or 'WAIT'? ").upper() 
    if action == "SWIM":
        #If swim is selected
        print ("Found treasure")
    else:
        #If wait is selected
        print ("Nothing found sadly!")

#If the choosen direction is right
elif direction == "RIGHT":
    #This is the immediate response 
     print ("You got caught by pirates.")
else:
    #If user input something unkown
     print ("Got lost.")

