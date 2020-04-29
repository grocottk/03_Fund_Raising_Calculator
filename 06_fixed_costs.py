
# Fund Raising Calculator Component 6
# Asks the user for the fixed costs associated with their product, then prints the fixed costs subtotal

# Setting 'total' variable to zero:

total = 0

# Lists:

item_cost = []
fixed_costs = []

# Main Routine:

print("Please enter the fixed costs associated with your product below:")
print()

# Get inputs and add to the mini list

item = ""

while item.lower() != "xxx":

    item_cost = []

    item = input("What is the name of the fixed cost? ")

    # If the user enters the exit code, break the loop

    if item.lower() == "xxx":

        break

    # Ask the user for the cost of the item
    # (Eventually, replace this with a number checking function)

    cost = float(input("What is the fixed cost in NZD? "))

    # Add both the item name and cost to the mini list

    item_cost.append(item)
    item_cost.append(cost)

    # Add the mini lists to the master list

    fixed_costs.append(item_cost)

# Add the costs of the items into a variable:

for item in fixed_costs:

    total += item[1]

# Prints the Subtotal

print("The subtotal of the fixed costs is ${:.2f}".format(total))
