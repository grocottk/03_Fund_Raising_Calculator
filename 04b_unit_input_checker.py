
# Fund Raising Calculator Component 4
# Checks the entered name of the project, as well as the number input of desired units

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
