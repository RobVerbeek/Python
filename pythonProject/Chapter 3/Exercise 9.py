# Write a program that allows the user to print the following series of integers, for each number
# between 10 and 20.
for count in range(10, 20+1, 2):
    for i in range(count, 0-1, -1):
        print(i, end=" ")
    print("")

