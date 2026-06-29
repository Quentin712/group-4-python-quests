direction = input("GO 'LEFT' or 'RIGHT'? ")
direction = direction.upper()

if direction == "LEFT":
    action = input ("Want to 'SWIM' or 'WAIT'? ").upper() 
    if action == "SWIM":
        print ("Found treasure")
    else:
        print ("Nothing found sadly!")

elif direction == "RIGHT":
     print ("You got caught by pirates.")
else:
     print ("Got lost.")

