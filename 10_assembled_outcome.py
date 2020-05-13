
# Fund Raising Calculator Assembled Outcome
# Assembles a collection of previously created Components in order to create a program that meets the specifications
# ... of a Fund Raising Calculator

# Functions:

# Statement Generator(Finds the length of a message, and prints characters above and below that equal the
# ...length of the message) [Taken from MQA_Post_Usability_Testing_1.0 Gist created on October 29 2019]:


def statement_generator(message, character):
    print()
    print(len(message) * character)
    print(message)
    print(len(message) * character)
    print()

# Number Checking Function (For numbers greater than zero):


def number_checker(question):

    # Defines Error Message

    error = "Please enter a number that is more than zero."

    # Beginning of Loop

    valid = False
    while not valid:

        try:

            response = float(input(question))

            # If response is less than or equal to zero, print the error message

            if response <= 0:
                print(error)

            else:

                # Otherwise, return the user's response

                return response

        # If a value error is present, print the error message

        except ValueError:
            print(error)

# Blank Checking Function (Checks that the inputs given for a value do not have numbers in them and are not blank):


def not_blank(question):

    # Defines error message

    error = "Sorry, but you must enter a string as your project name. You cannot have numbers in your project name."

    # Beginning of loop

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

        # If the response to the question is blank, print an error message

        if response == "":
            print()
            print("Sorry, but you must enter something as your project name. You cannot leave it blank.")
            print()
            continue

        # If the response to the question has other errors, print the error message

        elif has_errors != "":
            print()
            print(error)
            print()
            continue

        # Otherwise, return the response

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

expenses.sort(key=lambda x: x[1], reverse=1)

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
