
# Fund Raising Calculator Assembled Outcome
# Assembles a collection of previously created Components in order to create a program that meets the specifications
# ... of a Fund Raising Calculator

# Functions:

# Statement Generator (Taken from MQA_Post_Usability_Testing_1.0 Gist created on October 29 2019)


def statement_generator(message, character):
    print()
    print(len(message) * character)
    print(message)
    print(len(message) * character)
    print()

# Number Checking Function


def number_checker(question):
    error = "Please enter a number that is more than zero."

    valid = False
    while not valid:

        try:
            response = float(input(question))

            if response <= 0:
                print(error)

            else:

                return response

        except ValueError:
            print(error)

# Blank Checking Function:


def not_blank(question):

    error = "Sorry, but you must enter a string as your project name. You cannot have numbers in your project name."

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        # Look at each character in string, if any characters are numbers, give an error

        for letter in response:
            if __name__ == '__main__':
                if letter.isdigit():
                    has_errors = "yes"
                    break

        if response == "":
            print()
            print("Sorry, but you must enter something as your project name. You cannot leave it blank.")
            print()
            continue

        elif has_errors != "":
            print()
            print(error)
            print()
            continue

        else:
            return response

# Lists:


item_cost = []
expenses = []

# Main Routine:


# Asks user for their product name

project_name = not_blank("What is the name of your project? ")

# Asks user for their desired number of units

units = number_checker("What is your desired number of units? ")


# Asks user for the name and cost of their expenses

# Get inputs and add to the mini list

item = ""

while item.lower() != "xxx":

    item_cost = []

    item = input("What is the name of the item? ")

    # If the user enters the exit code, break the loop

    if item.lower() == "xxx":

        break

    # Ask the user for the cost of the item
    # (Eventually, replace this with a number checking function)

    cost = float(input("How much does that item cost in NZD? "))

    # Add both the item name and cost to the mini list

    item_cost.append(item)
    item_cost.append(cost)

    # Add the mini lists to the master list

    expenses.append(item_cost)


# Sorts mini lists

# To sort by cost:

expenses.sort(key=lambda x: x[1], reverse = 1)

# Output:

print()

print("Items by cost (Highest to Lowest)")

for item in expenses:

    print("{}: ${:.2f}".format(item[0], item[1]))

print()

# To sort Alphabetically:

expenses.sort(key=lambda x: x[0])

print("Items in Alphabetical Order (A to Z)")

for item in expenses:

    print("{}: ${:.2f}".format(item[0], item[1]))
