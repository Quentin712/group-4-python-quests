#Asks user for a password
password = input ("Enter password: ")

#This is to check if the user inputs the same exact password "Maniac"
if password == "Maniac":
    #If it matches Access is granted
    print("Access Granted")
else: 
    #If the password don't match Access is denied
    print("Access Denied")
