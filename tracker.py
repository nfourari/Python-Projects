
# Function to set goals for the week
def load_goals(goals):

    print("Set your goals for the week!")

    # Asks user for categories and adds them to goals dictionary
    category_1 = input("Enter a category for your goal:\n")
    goals[category_1] = int(input("Enter your target for "+category_1+":\n"))

    category_2 = input("Enter a category for your goal:\n")
    goals[category_2] = int(input("Enter your target for "+category_2+":\n"))

    category_2 = input("Enter a category for your goal:\n")
    goals[category_2] = int(input("Enter your target for "+category_2+":\n"))


# Function to imput data for the week
def load_data():

    # Dictionary to store data for the week
    values = {}

    print("Enter your data with the category and measurement.")
    print("Type 'done' when done for today.")

    # Prompting user for category
    category = input("Enter category:\n")

    # While loop until user inputs done
    while category != "done":
        value = int(input("Enter value:\n"))

        # Checking if the category input is in values dictionary and asking user if they want to
        # add to the value or replace the category and value
        if category in values:
            choice = input("You have a value for "+category+".\nDo you want to (1) Add to "+category+", or (2) Replace "+category+"?\n")
            if (choice == "1"):
                values[category] += value
            else:
                values[category] = value
        # Adding category to dictionary if it does not exist
        else:
            values[category] = value

        # Asking for new category until user inputs done and then returning values dictionary
        category = input("Enter category:\n")

    return values
    
                
# Function comparing the data at the end of the week to the goals set at the beginning of the week
def compare(goals, data):

    # Variable to keep track of 
    goals_met = 0

    # For loop to go through the keys in goals dictionary and compare their values to the keys in the data dictionary
    for key in goals:
        if key in data:
            if data[key] >= goals[key]:
                goals_met += 1

    # Returing 1 if the user meets 3 goals
    if goals_met > 2:
        return 1
    
    return 0
        


def main():

    # Two dictionaries storing goals and data for the week
    goals = {}
    data = {}

    # Variable to count how many days the user meets all 3 goals
    count = 0

    # Calling load goals function and passing in the goals dictionary
    load_goals(goals)
    

    # Printing out the days of the week and storing the data to the dictionary
    print("\nIt's Monday")
    data = load_data()
    count += compare(goals, data)

    print("\nIt's Tuesday")
    data = load_data()
    count += compare(goals, data)
    
    print("\nIt's Wednesday")
    data = load_data()
    count += compare(goals, data)

    print("\nIt's Thursday")
    data = load_data()
    count += compare(goals, data)

    print("\nIt's Friday - Happy Friday!")
    data = load_data()
    count += compare(goals, data)

    print("\nIt's Saturday")
    data = load_data()
    count += compare(goals, data)

    print("\nIt's Sunday")
    data = load_data()
    count += compare(goals, data)

    print("\nYou hit your goals",count,"times this week!")



main()
