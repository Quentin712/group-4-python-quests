#In this quest, we want to generate number from 1 to 20 and check it it even or not.
#We are going to use for-loop for generating numbers and if- statement to check if it even or not 
for i in range(1, 21):
    #The range generates numbers from 1 to 20 excluding the last number which is 21
    if i % 2 == 0:
        #Here we are checking if the number is even or not, if it is even then it will print it
        #% means remainder if i is divided by 2 
        #And we know that for a number to be even, the remainder of the division by 2 must be 0 
        print(i)
        print("Even number") 
    else:
        #Otherwise it will be an odd number 
        print(i)
        print("Odd number")
