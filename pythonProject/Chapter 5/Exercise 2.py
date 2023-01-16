# Use a List of numbers in your program. Write a program that generates a new List that contains the
# same numbers but all even numbers are in the first part of the List and the odd numbers at the end.

numbers_list = [23, 12, 54, 85, 64, 91]
new_list = []

print(numbers_list)
for i in numbers_list:
    if i % 2 == 0:
        new_list.insert(0, i)
    else:
        new_list.append(i)
print(new_list)

