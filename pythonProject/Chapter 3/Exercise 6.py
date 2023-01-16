# Write a program that allows the user to print a series of numbers on the screen, each time separated
# by 3 dots.
# The user first fills in a positive start number, then all numbers from that number up to and including
# 0 are printed on the screen.
number = int(input("Enter a number: "))
#
if number > 0:
    print(number, "...", end=" ")
    while number > 0:
        number -= 1
        print(number, "...", end=" ")
