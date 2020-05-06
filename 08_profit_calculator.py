# Fund Raising Calculator Component 8
# Asks the user how much profit they require (in either a percentage or amount), then add this to the total cost
# ... to find the total sales needed

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

total = 1000


# Main Routine:


# Ms. Gottschalk's String Checker (Licenced under the 'GNU GENERAL PUBLIC LICENSE') [Updated for use in this program]

def string_checker(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("sorry that is not a valid response")


amount_percentage = ["amount", "percentage"]

profit_unit = string_checker("Would you like to enter your desired profit as "
                             "an amount or a percentage? ", amount_percentage)

# End of Ms. Gottschalk's String Checker (Licenced under the 'GNU GENERAL PUBLIC LICENSE')

# Checks to see which unit was chosen, then asks questions accordingly:

# If the profit is as a percentage:

if profit_unit == "percentage":

    percentage = number_checker("What percentage of profit would you like to make? ")

    # Multiplying Profit by the total, then adding to the total again (Credit to scanftree.com)

    revenue_required = float((percentage / 100) * total) + float(total)

# If the profit is as an amount:

elif profit_unit == "amount":

    amount = number_checker("What amount of profit in NZD would you like to make? ")

    # Add profit to total (Credit to scanftree.com)

    revenue_required = float(amount) + float(total)

print("The amount of revenue that you require to reach your profit goal is ${:.2f}".format(revenue_required))
