
# Fund Raising Calculator Component 7
# Combines Components 5 and 6 in order to find the overall total by adding the two subtotals

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

# Defining 'variable_subtotal' variable:

variable_subtotal = 0

# Setting 'fixed_subtotal' variable to zero:

fixed_subtotal = 0

# Lists:

fixed_item_cost = []
fixed_costs = []

variable_item_cost = []
variable_costs = []

# Main Routine:

# Variable Costs ______________________________________________________________________________________________________

# Ask user for their required number of units

units_required = number_checker("What is your desired number of units? ")

print("Please enter the variable costs associated with your product below:")
print()

# Get inputs and add to the mini list

variable_item = ""

while variable_item.lower() != "xxx":

    variable_item_cost = []

    variable_item = input("What is the name of the variable cost? ")

    # If the user enters the exit code, break the loop

    if variable_item.lower() == "xxx":

        break

    # Ask the user for the cost of the item
    # (Eventually, replace this with a number checking function)

    variable_cost = float(input("What is the fixed cost in NZD? "))

    # Add both the item name and cost to the mini list

    variable_item_cost.append(variable_item)
    variable_item_cost.append(variable_cost)

    # Add the mini lists to the master list

    variable_costs.append(variable_item_cost)

# Add the costs of the items from the list into a variable:

for item in variable_costs:

    variable_subtotal += item[1]

# Calculates Subtotal:

calculated_variable_subtotal = variable_subtotal * units_required

# Prints the Subtotal

print("The subtotal of the variable costs is ${:.2f}".format(calculated_variable_subtotal))

# Fixed Costs _________________________________________________________________________________________________________

print("Please enter the fixed costs associated with your product below:")
print()

# Get inputs and add to the mini list

fixed_item = ""

while fixed_item.lower() != "xxx":

    fixed_item_cost = []

    fixed_item = input("What is the name of the fixed cost? ")

    # If the user enters the exit code, break the loop

    if fixed_item.lower() == "xxx":

        break

    # Ask the user for the cost of the item
    # (Eventually, replace this with a number checking function)

    fixed_cost = float(input("What is the fixed cost in NZD? "))

    # Add both the item name and cost to the mini list

    fixed_item_cost.append(fixed_item)
    fixed_item_cost.append(fixed_cost)

    # Add the mini lists to the master list

    fixed_costs.append(fixed_item_cost)

# Add the costs of the items into a variable:

for item in fixed_costs:

    fixed_subtotal += item[1]

# Prints the Subtotal

print("The subtotal of the fixed costs is ${:.2f}".format(fixed_subtotal))

# Total Calculations:

total = calculated_variable_subtotal + fixed_subtotal

print(total)
