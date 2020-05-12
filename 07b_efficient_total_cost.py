
# Fund Raising Calculator Component 7b
# Combines Components 5 and 6 in order to find the overall total by adding the two subtotals. The original
# ... version of this code was inefficient, an issue which will be addressed in this component

# Functions:

# Number Checking Function (for numbers greater than zero)


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

# Subtotal Finding Function (uses units_required in order to swap between Fixed and Variable Costs)


def get_costs(units_required, fixed):

    # Defining list that holds all of the costs and names

    all_items = []

    # Defines cost

    costs = all_items

    # Defines subtotal

    subtotal = 0

    # If the require input is fixed costs, define units required as one

    if fixed == "yes":

        units_required = 1

    variable_item = ""

    while variable_item.lower() != "xxx":

        # Holds each 'row' of the price breakdown

        item_cost = []

        variable_item = input("What is the name of the variable cost? ")

        # If the user enters the exit code, break the loop

        if variable_item.lower() == "xxx":

            break

        # Ask the user for the cost of the item
        # (Eventually, replace this with a number checking function)

        variable_cost = float(input("What is the variable cost in NZD? "))

        # Add both the item name and cost to the mini list

        item_cost.append(variable_item)
        item_cost.append(variable_cost)

        # Add the mini lists to the master list

    all_items.append(costs)

    # Add the costs of the items from the list into a variable:

    for item in costs:

        subtotal += item[1]

    # Calculates Subtotal:

    calculated_subtotal = subtotal * units_required

    # Prints the Subtotal

    print("The subtotal of the variable costs is ${:.2f}".format(calculated_subtotal))
    print()
