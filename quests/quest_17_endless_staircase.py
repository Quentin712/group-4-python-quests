#In this quest, we want the block of code to keep executing until the count reaches to 5 
#In this we are going to use while-loop as it will keep looping or executing as long as the condition is true
#Starting from zero
count = 0 
while count < 5:
    print(f"Step {count}")
    count += 1
    #We have to manually increase the count each time, otherwise this will repeat forever
print("You have reached the top")
#If it reaches 5, it will stop and print the above message 