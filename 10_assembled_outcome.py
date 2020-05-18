
# Fund Raising Calculator Assembled Outcome
# Assembles a collection of previously created Components in order to create a program that meets the specifications
# ... of a Fund Raising Calculator

# Functions:

# Statement Generator (Finds the length of a message, and prints characters above and below that equal the
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

    error = "Sorry, but you must enter a string as your name. You cannot have numbers in your name."

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

# Subtotal Finding Function (uses units_required in order to swap between Fixed and Variable Costs)


def get_subtotal(units_required, fixed):

    # Defining Lists:

    # Defining Costs List

    costs = []

    # Defining Variables:

    # Defining 'subtotal' variable:

    subtotal = 0

    # If the required input is fixed costs, define units required as one

    if fixed == "yes":

        units_required = 1

        print("Please enter the fixed costs associated with your product below:")

    # Otherwise, ask fot the variable costs associated

    else:

        print("Please enter the variable costs associated with your product below:")

    # Get inputs and add to the mini list

    item = ""

    while item.lower() != "xxx":

        item_cost = []

        item = not_blank("What is the name of the cost? ")

        # If the user enters the exit code, break the loop

        if item.lower() == "xxx":
            break

        # Ask the user for the cost of the item

        cost = number_checker("What is the cost in NZD? ")

        # Add both the item name and cost to the mini list

        item_cost.append(item)
        item_cost.append(cost)

        # Add the mini lists to the master list

        costs.append(item_cost)

    # Add the costs of the items from the list into a variable:

    for item in costs:
        subtotal += item[1]

    # Calculates Subtotal:

    calculated_subtotal = subtotal * units_required

    # Prints the Subtotal

    print("The subtotal of these costs is ${:.2f}".format(calculated_subtotal))
    print()

    return calculated_subtotal

# Main Routine:

# Ask user for their required number of units and defines function as variable


variable_subtotal = get_subtotal(number_checker("What is your desired number of units? "), "no")

# Defines the number of required units as one and the function as fixed


fixed_subtotal = get_subtotal(1, "yes")

# Finds the total by using the two subtotals

total = fixed_subtotal + variable_subtotal

# Prints message telling the user the total of their two subtotals

print("The total added cost of both subtotals is ${:.2f}".format(total))
