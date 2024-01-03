# Noah Fourari
# Program 7 - Smoothie Recipies
# COP 2500
# Oct 25, 2023

# Function to ask the user how many of each ingredient they have and add them to the list
def load_list(smoothie_list):

    print("Welcome to our Smoothie Recipe Analyzer!")
    smoothie_list.append(float(input("\nHow many bananas do you have?\n")))
    smoothie_list.append(float(input("How many strawberries do you have?\n")))
    smoothie_list.append(float(input("How many blueberries do you have?\n")))
    smoothie_list.append(float(input("How many cups of spinach do you have?\n")))
    smoothie_list.append(float(input("How many avocados do you have?\n")))
    return smoothie_list

# Menu function to prompt the user to choose an option for what they would like to do
def menu():

    print("\nWhat would you like to do?")
    print("1 - View Ingredients")
    print("2 - Update Ingredients")
    print("3 - Make a Smoothie")
    print("4 - Quit")
    choice = int(input(""))
    return choice

# Function displaying all the ingredients the user said they have by using index of each
# ingredient in the list
def view_ingredients(smoothie_list):
    print("\nAmount of Ingredients:")
    print("Bananas:", smoothie_list[0])
    print("Strawberries:", smoothie_list[1])
    print("Blueberries:", smoothie_list[2])
    print("Spinach:", smoothie_list[3],"cups")
    print("Avocados:", smoothie_list[4])
          
    
# Function allowing user to update amount of each ingredient using index values
# and casting them as floats
def update_ingredients(smoothie_list):
    smoothie_list[0] = float(input("\nHow many bananas do you have?\n"))
    smoothie_list[1] = float(input("How many strawberries do you have?\n"))
    smoothie_list[2] = float(input("How many blueberries do you have?\n"))
    smoothie_list[3] = float(input("How many cups of spinach do you have?\n"))
    smoothie_list[4] = float(input("How many avocados do you have?\n"))
    return smoothie_list

# Function that allows the user to make their own smoothie with ingredients of their choosing
def make_smoothie(smoothie_list):
    # Setting default values and creating flag variable
    drink_score = 0
    health_score = 2
    flag = 0

    # Setting yes and no as boolean values
    yes = True
    no = False

    # If statements to see if their are enough of that ingredient to make a smoothie with
    bananas = input("\nWill you use bananas?\n")
    if (bananas == "yes"):
        if (smoothie_list[0]<1):
            flag = 1
        
    
    strawberries = input("Will you use strawberries?\n")
    if (strawberries == "yes"):
        if (smoothie_list[1]<5):
            flag = 1
        
    blueberries = input("Will you use blueberries?\n")
    if (blueberries == "yes"):
        if (smoothie_list[2]<12):
            flag = 1
    
    spinach = input("Will you add spinach?\n")
    if (spinach == "yes"):
        if (smoothie_list[3]<1):
            flag = 1
        
    avocados = input("Will you add avocado?\n")
    if (avocados == "yes"):
        if (smoothie_list[4]<0.5):
            flag = 1
    # If statement to subtract amount of ingredient used in one smoothie from total amount of ingredient
    if (flag == 0):
        if (bananas == "yes"):
            smoothie_list[0] -= 1
        if (strawberries == "yes"):
            smoothie_list[1] -= 5
        if (blueberries == "yes"):
            smoothie_list[2] -= 12 
        if (spinach == "yes"):
            smoothie_list[3] -= 1
        if (avocados == "yes"):
            smoothie_list[4] -= 0.5
        
        # Calculating drink scores based on avocados and spinach
        if (spinach == "yes" and avocados == "yes"):
            print("Your recipe scored a Drink Score of 0. Yuck!")
            print("Your recipe scored a Health Score of 2. It will be super healthy!")
        elif (spinach =="yes" or avocados =="yes"):
            print("Your recipe scored a Drink Score of 1. It will be delicious!")
            print("Your recipe scored a Health Score of 1. It is good to go!")
        else:
            print("Your recipe scored a Drink Score of 1. It will be delicious!")
            print("Your recipe scored a Health Score of 0. It probably tastes good though.")

    # Else statement if there is not enough of a certain ingredient needed to make a smoothie
    else:
        print("Sorry, this recipe cannot be completed.")

    return smoothie_list

# Main function calling all other functions
def main():
    # List of ingredients
    smoothie_list = []
    smoothie_list = load_list(smoothie_list)

    # Default value for option
    option = 0

    # While loop that determines what function is carried out based on the option the user picks
    while option != 4:
        option = menu()
        if (option == 1):
            view_ingredients(smoothie_list)
        if (option == 2):
            smoothie_list = update_ingredients(smoothie_list)
        if (option == 3):
            smoothie_list = make_smoothie(smoothie_list)

# Calling main function
main()
