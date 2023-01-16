# Write a program to read a series of numbers  (stop the input by entering 0).
# Print the largest number and the smallest number entered as well as the difference between those
# numbers.
smallest = number = int(input("Enter a number, stop by entering 0: "))
biggest = 0
#
while number != 0:
    if number > smallest:
        biggest = number
    elif number < smallest:
        smallest = number
    number = int(input("Enter a number, stop by entering 0: "))
print("the smallest number is:", smallest, "the biggest number is:", biggest)






