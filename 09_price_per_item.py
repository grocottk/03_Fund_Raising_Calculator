
# Fund Raising Calculator Component 9
# Asks user for number of items that will be sold and the total amount of required revenue finds a recommended
# ... price per item taking into account real world factors

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

# Main Routine:


# Asks the user their desired number of units and required revenue

units = number_checker("What is your desired number of units? ")

revenue_required = number_checker("What is the total amount of revenue "
                                  "that you require to meet your desired profit? ")

# Divides the revenue required by the number of units that will be sold

price_per_unit = float(revenue_required) / float(units)

# Tells the user their calculated price per item

print("Your calculated price per unit is:")
print()
print("${:.2f} per unit".format(price_per_unit))

# Calculates practical price per unit: [Enter equation below]

p_p_p_unit = 0

# Tells the user their practical price per unit

print("Your practical price per unit is:")
print()
print("${:.2f} per unit".format(p_p_p_unit))
