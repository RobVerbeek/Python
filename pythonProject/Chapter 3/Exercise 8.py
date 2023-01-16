# Write a program that asks for a digit followed by the input of 10 numbers. As a result you get the
# number of numbers that ends on this digit.
# Make sure that the output text changes appropriately when only 1 number ends on the final digit.
end_number = int(input("What final digit do you want the numbers to end on: "))
number = int(input("Enter a number: "))
count = 0
for i in range(1, 10):
    if number % 10 == end_number:
        count += 1
    number = int(input("Enter a number: "))
if count > 1:
    print(count, "out of 10 numbers end on", end_number)
else:
    print("Only", count, "out of 10 numbers end on", end_number)


