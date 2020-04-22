
# Fund Raising Calculator Component 4
# Checks the entered name of the project, as well as the number input of desired units

# Blank Checking Function:


def not_blank(question):

    error = "Sorry, but you must enter a string as your project name. You cannot have numbers in your project name."

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

        if response == "":
            print()
            print("Sorry, but you must enter something as your project name. You cannot leave it blank.")
            print()
            continue

        elif has_errors != "":
            print()
            print(error)
            print()
            continue

        else:
            return response

# Main Routine:

project_name = not_blank("What is the name of your project? ")

print()
print("The name of your project is {}".format(project_name))
