#This asks the user to enter their age and make sure its a number 
age = input ("Enter age: ")
age = int (age)

#This asks the user to enter their gold coin and make sure its a number 
gold_coins = input ("Enter gold coins: ")
gold_coins = int (gold_coins)

#The condition of age and gold coins must be met inorder to proceed
if age>= 18 and gold_coins >=20:
    #If both conditions are met,they can enter
    print ("Club entry accepted.")
else:
    #If even one of the conditions is not met, entry is denied
    print ("Club entry denied.")
