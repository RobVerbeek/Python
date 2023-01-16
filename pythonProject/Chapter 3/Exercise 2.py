# Write a program to count how many zeros and sixes you can find in a number.
number = int(input("Enter a number: "))
sixes = 0
zeros = 0
#
while number != 0:
    if number % 10 == 0:
        zeros += 1
    elif number % 10 == 6:
        sixes += 1
    number //= 10
print("The amount of sixes:", sixes, "and the amount of zeros: ", zeros)
