
# Setting variables for gender and age
gender = input("Do you want to use the target heart rate for men or women?\n")
age = int(input("How old are you?\n"))

# If statement to determine whether to use target for men or women
if gender == "men":
    rate = 226 - age
else:
    rate = 220 - age

# Setting starting values for all heart rates and the times the target was hit
total = 0
target_reached = 0

# Prompting user to enter heart rates
print("Please enter your recorded heart rates:")

#Setting heart rate to 1 to enter the while loop
heart_rate = 1

# While loop to continue until the user enters -1
# Also tracking whether or not the user hit the target
while (heart_rate > 0):
    heart_rate = int(input())
    if (heart_rate >= rate):
        target_reached += 1
    total += 1

# Printing the times the user hit the target out of the total heart rates entered
print("You hit your target heart rate ",target_reached," times out of ",total-1,"!",sep="")
        
        
