# test if a negative or positive number ends with a specific number
number = int(input("Enter a number: "))
end_number = int(input("What last number do you want to test with: "))
# print
if number < 0:
    print("Negative numbers will not be tested.")
elif number % 10 == end_number:
    print(number, "ends with", end_number)
else:
    print(number, "does not end with", end_number)
