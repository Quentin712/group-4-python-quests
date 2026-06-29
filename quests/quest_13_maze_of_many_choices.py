#This asks user to enter a score
score = input ("Enter score (0-100): ")
#This makes sure that what ever is enter is a number otherwise it brings error
score = int (score)

#This is checks the grade the user input where it falls inorder to give the feedback 
if score >= 90:
    print ("A")
elif score >= 80:
    print ("B")
elif score >= 70:
    print ("C")
else:
    #This is what is printed if the user input anything below 70
    print ("Needs Improvement")
