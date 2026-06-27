#calculate_area will take length and width as inputs
#then multiple them together, and return the result.
def calculate_area(length, width):
    #Return sends the area back so we can store and use it outside the function
    return length * width
#We call the function twice with different values to show it works for any size 
#Then the return result will be stored in a variable each time 
area_one = calculate_area(4, 5)
area_two = calculate_area(10, 2)
#finally it will print the stored results here.
print(f"The first room has an area of {area_one}.")
print(f"The second room has an area of {area_two}.")
