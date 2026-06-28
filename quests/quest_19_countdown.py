#In this quest, we want to simulate a rocket launch where we count from 10 to 1.
#To do this we want to use the for-loop with increment
#Counting down from 10 to 1, then print "Blast off" 
for i in range(10, 0, -1):
    #Here it will stop before 0 so the last number printed is 1 
    #-1 is the increment that helps us step backwards by 1 each time
    print(i)
print("Blastoff!")
#Once the loop finishes it will print the above message
