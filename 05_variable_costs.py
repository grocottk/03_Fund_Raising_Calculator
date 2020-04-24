
# Fund Raising Calculator Component 5
# Asks the user for the variable costs associated with their product, then multiplies them by the units required.
# ...A subtotal is then created, which is shown to the user.

# Functions:

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

# Defining Variables:


# Defining 'total' variable:

total = 0

# Variable Costs List:

variable_costs = [["Nail", 3.0], ["Wooden Plank", 12.0], ["Rope", 7.5], ["Glue", 16.5]]

# Main Routine:

# Add the costs of the items from the list into a variable:

for item in variable_costs:

    total += item[1]

# Ask user for their required number of units

units_required = number_checker("What is your desired number of units? ")

# Calculates Subtotal:

variable_subtotal = total * units_required

# Prints the Subtotal

print("The subtotal of the variable costs is ${:.2f}".format(variable_subtotal))
