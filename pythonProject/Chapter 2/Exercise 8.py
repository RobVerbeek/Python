# pizza party
pizza = int(input("How many pizzas are there: "))
wine = int(input("How many bottles of wine are there: "))
#
if wine >= 5 and pizza >= 5:
    if wine >= pizza * 2 or pizza >= wine * 2:
        print("This is a fantastic party")
    else:
        print("This is a good party")
elif wine <= 5 or pizza <= 5:
    print("This party is stupid")
