
# Fund Raising Calculator Component 3
# Uses mini lists as a data set in order to find the average of values in the list

expenses = [["Nail", 3.0], ["Wooden Plank", 12.0], ["Rope", 7.5], ["Glue", 16.5]]

total = 0

# Add the costs of the items into a list:

for item in expenses:

    total += item[1]

# Calculates Average

average = total / len(expenses)

print("The average price of the items in the list is ${:.2f}".format(average))
