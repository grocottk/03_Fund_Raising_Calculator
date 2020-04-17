
# Component 1
# Adds given Items and costs into multiple mini lists, which are then entered into a larger list

# Lists:

item_cost = []
expenses = []

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


print(expenses)
