
# Fund Raising Calculator Component 2
# Sorts the mini lists with the product name and price, that are a part of the larger list of all costs

expenses = [["Nail", 3.0], ["Wooden Plank", 12.0], ["Rope", 7.5]]

# To sort by cost:

expenses.sort(key=lambda x: x[1], reverse=1)

# Output:

print("Items by cost (Highest to Lowest)")

for item in expenses:

    print("{}: ${:.2f}".format(item[0], item[1]))

print()

# To sort Alphabetically:

expenses.sort(key=lambda x: x[0])

print("Items in Alphabetical Order (A to Z)")

for item in expenses:

    print("{}: ${:.2f}".format(item[0], item[1]))
