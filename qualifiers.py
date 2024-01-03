
# Menu function do prompt user with choices
def menu():
    print("\nWhat would you like to do?")
    print("1 - Add a time")
    print("2 - Delete a time")
    print("3 - Compare times")
    print("4 - Check qualifiers")
    print("5 - Quit")
    choice = int(input(""))
    return choice

# Function that allows user to add times to racer_a and racer_b list
def add(racer_a, racer_b):
    racer = input("Which racer is adding a time?\n")
    if racer == "A":
        racer_a.append(float(input("What is the time to be added?\n")))
    if racer == "B":
        racer_b.append(float(input("What is the time to be added?\n")))

# Function that allows user to delete a time or race from lists
def delete(racer_a, racer_b):

    # Asking user what racer and if wrong anser display message
    racer = input("Which racer is deleting a time?\n")
    if (racer != "A" and racer != "B"):
        print("Could not interpret racer. Please use A or B")
        return
    # If user chooses A they can delete a race or time from racer_a list
    if (racer == "A"):
        delete = input("Delete a time or delete a race?\n")
        if (delete == "Time" or delete == "time"):
            choice = float(input("What time should be deleted?\n"))
            racer_a.remove(choice)
        elif (delete == "Race" or delete == "race"):
           race = int(input("What race should be deleted?\n"))
           racer_a.pop(race - 1)
        else:
            print("Could not interpret deletion. Please use time or race.")

    # If user chooses B they can delete a race or time from racer_b
    if (racer == "B"):
        delete = input("Delete a time or delete a race?\n")
        if (delete == "Time" or delete == "time"):
            choice = float(input("What time should be deleted?\n"))
            racer_b.remove(choice)
        elif (delete == "Race" or delete == "race"):
           race = int(input("What race should be deleted?\n"))
           racer_b.pop(race - 1)
        else:
            print("Could not interpret deletion. Please use time or race.")
        
        
# Function that compares the times of racer A and racer B
def compare(racer_a, racer_b):

    length_a = len(racer_a)
    length_b = len(racer_b)

    if (length_a <= length_b):
        number = length_a
    if (length_a >= length_b):
        number = length_b

    # Statement for if one of the racers has no times
    if (length_a == 0 or length_b == 0):
        print("At least one racer has no times!\n")
        return

    # Showing how many races a and b have data for
    if (length_a != length_b):
        print("Racer A has data for " + str(length_a) + " races.")
        print("Racer B has data for " + str(length_b) + " races.")

    # Seeing how which races each racer won or tied
    print("We will compare the first " + str(number) + " races.")
    for i in range (number):
        if (racer_a[i] < racer_b[i]):
            print("Racer A has won race #" + str(i+1) + "!")
        if (racer_b[i] < racer_a[i]):
            print("Racer B has won race #" + str(i+1) + "!")
        if (racer_a[i] == racer_b[i]):
            print("The racers tie race #" + str(i+1) + ".")
        

# Function that determines which racers qualified
def qualifiers(racer_a, racer_b, time):

    for i in range (3):
        print("Qualifier #" + str(i+1) + ":")
        if (racer_a[i] > time[i] and racer_b[i] > time[i]):
          print("Neither racer qualified.")
        if (racer_a[i] <= time[i]):
            print("Racer A Qualifies!")
        if (racer_b[i] <= time[i]):
            print("Racer B Qualifies!")
    
# Main function with all three lists and inputs to add values to the list
def main():

    time = []

    racer_a = []
    
    print("Enter times for Racer A:")
    a = float(input("Race #1: "))
    racer_a.append(a)
    a = float(input("Race #2: "))
    racer_a.append(a)
    a = float(input("Race #3: "))
    racer_a.append(a)
    
    racer_b = []
    
    print("\nEnter times for Racer B:")
    b = float(input("Race #1: "))
    racer_b.append(b)
    b = float(input("Race #2: "))
    racer_b.append(b)
    b = float(input("Race #3: "))
    racer_b.append(b)

    print("\nEnter times for the qualifiers:")
    race_1 = int(input("Race #1: "))
    time.append(race_1)
    
    race_2 = int(input("Race #2: "))
    time.append(race_2)

    race_3 = int(input("Race #3: "))
    time.append(race_3)

    option = 0

    # While loop to call different functions based on option user chooses
    while option != 5:
        option = menu()
        if (option == 1):
            add(racer_a, racer_b)
        if (option == 2):
            delete(racer_a, racer_b)
        if (option == 3):
            compare(racer_a, racer_b)
        if (option == 4):
            qualifiers(racer_a, racer_b, time)
    


main()
