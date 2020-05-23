
# Fund Raising Calculator Post Usability Testing Outcome
# This is the outcome of the Fund Raising Calculator after Usability Testing, where the main feedback related to
# ... the usability was in regards to a lack of instructions. This is the final build og my Fund Raising Calculator.

# *** Functions: ***

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
            print("Sorry, but you must enter something as your name. You cannot leave it blank.")
            continue

        # If the response to the question has other errors, print the error message

        elif has_errors != "":
            print(error)
            continue

        # Otherwise, return the response

        else:
            return response

# Subtotal Finding Function (uses units_required in order to swap between Fixed and Variable Costs)


def get_subtotal(units_needed):

    # Defining Lists:

    # Defining Costs List

    costs = []

    # Defining Variables:

    # Defining 'subtotal' variable:

    subtotal = 0

    # If the units are equal to one, ask for the fixed costs associated with the product

    if units_needed == 1:

        print("Please enter the fixed costs associated with your product below:")

    # Otherwise, ask fot the variable costs associated

    else:

        print("Please enter the variable costs associated with your product below:")

    # Get inputs and add to the mini list

    individual_item = ""

    while individual_item.lower() != "xxx":

        item_cost = []

        individual_item = not_blank("What is the name of the cost? ")

        # If the user enters the exit code, break the loop

        if individual_item.lower() == "xxx":
            break

        # Ask the user for the cost of the item

        individual_cost = number_checker("What is the cost in NZD? ")

        # Add both the item name and cost to the mini list

        item_cost.append(individual_item)
        item_cost.append(individual_cost)

        # Add the mini lists to the master list

        costs.append(item_cost)

    # Add the costs of the items from the list into a variable:

    for item in costs:
        subtotal += item[1]

    # Calculates Subtotal:

    calculated_subtotal = subtotal * units_needed

    # Prints the Subtotal

    print("The subtotal of these costs is ${:.2f}".format(calculated_subtotal))
    print()

    return calculated_subtotal

# Ms. Gottschalk's String Checker (Licenced under the 'GNU GENERAL PUBLIC LICENSE') [Updated for use in this program]


def string_checker(question, to_check):

    # Loop while the string is not valid

    valid = False
    while not valid:

        # Defines response as the question, converted into all lower case

        response = input(question).lower()

        for item in to_check:

            # If the given response is equal to the item, return the response

            if response == item:
                return response

            # If the response is equal to the first item in the list, return the item

            elif response == item[0]:
                return item

        # Prints error message

        print("sorry that is not a valid response")

# End of Ms. Gottschalk's String Checker (Licenced under the 'GNU GENERAL PUBLIC LICENSE')

# Instruction Printing Function (Prints the Instructions to the program)
# Formatting Credit to 'The Python Cheat Sheet' and 'Noobmaster69'


def instructions():

    print('''The aim of this program is to intake raw costs from a fund raising entity,
and perform a series of equations in order to output various statistics,
including a recommended, practical, price per unit.

In this program, you will be asked to input a selection of costs,
both variable and fixed (entering 'xxx' once all applicable costs have been entered),
after which, a subtotal will be printed in both cases.

Following this, you will be required to enter the amount of profit that you desire to make,
as either a percentage or an amount. After this, a selection of prices will be printed,
concluding the program.

To begin the program, please enter the name of your chosen project,
followed by the number of units that are available for sale.

Disclaimer: This program is intended for hypothetical use, therefore,
costs are required to be created and entered by the user.
''')

# *** Main Routine: ***

# * Introduction: *

# Print title and introduction of Fund Raising Calculator


statement_generator("Welcome to the Fund Raising Calculator", "*")

# Prints the instructions to the program

instructions()

# Asks the user the name of their project

project_name = not_blank("What is the name of your project? ")

# * Receiving Costs: *

# Defines 'units_required' as the desired number of units

units_required = number_checker("What is the number of units that you intend to sell? ")
print()

# Enters 'units_required' variable into the 'get_subtotal' function

variable_subtotal = get_subtotal(units_required)

# Defines the number of required units as one

fixed_subtotal = get_subtotal(1)

# * Total Cost: *

# Finds the total by using the two subtotals

total = fixed_subtotal + variable_subtotal

# Prints message telling the user the total of their two subtotals

print("The total added cost of both subtotals is ${:.2f}".format(total))
print()

# * Finding desired Profit: *

# Defines 'amount_percentage' list

amount_percentage = ["amount", "percentage"]

# Asks the user whether they would like to enter their desired profit as an amount or a percentage
# ... (using the string checker)

profit_unit = string_checker("Would you like to enter your desired profit as "
                             "an amount or a percentage? ", amount_percentage)

# Checks to see which unit was chosen, then asks questions accordingly:

# If the profit is as a percentage:

if profit_unit == "percentage":

    percentage = number_checker("What percentage of profit would you like to make? ")

    # Multiplying Profit by the total, then adding to the total again (Credit to scanftree.com)

    revenue_required = float((percentage / 100) * total) + float(total)

# If the profit is as an amount:

else:

    amount = number_checker("What amount of profit in NZD would you like to make? ")

    # Add profit to total (Credit to scanftree.com)

    revenue_required = float(amount) + float(total)

print("The amount of revenue that you require to reach your profit goal is ${:.2f}".format(revenue_required))

# * Price Per Item: *

# Divides the revenue required by the number of units that will be sold

price_per_unit = float(revenue_required) / float(units_required)

# Tells the user their calculated price per item

print()
print("Your calculated price per unit is ${:.2f} per unit".format(price_per_unit))

# Calculates practical price per unit: [Enter equation below]

practical_unit = (float(revenue_required) / float(units_required)) * 1.25

# Tells the user their practical price per unit

print("Your practical price per unit is ${:.2f} per unit".format(round(practical_unit, 0)))

# *** Project Summary: ***

# Prints the project name

statement_generator(project_name, "~")

# Prints both subtotals

print("Calculated Variable Costs Subtotal: ${:.2f}".format(variable_subtotal))
print("Fixed Costs Subtotal: ${:.2f}".format(fixed_subtotal))

# Prints total project cost

print("Total Costs: ${:.2f}".format(total))

# Prints total revenue required

print("Total Revenue: ${:.2f}".format(revenue_required))

# Prints calculated and practical prices per unit

print("Calculated Price Per Unit: ${:.2f}".format(price_per_unit))
print("Practical Price Per Unit ${:.2f}".format(practical_unit))
