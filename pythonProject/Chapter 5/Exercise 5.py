# Use a List of numbers in your program.
# Write a program that replaces every 0 in the list with the largest odd number you can find on the
# right side of that 0. If there is no odd number to be found then the 0 just remains.
# no_list = [0, 42, 18, 17, 0, 19, 10, 5, 14]
no_list = [42, 18, 0, 37, 0, 2, 19, 10, 5, 14]

# loop through list find 0 find biggest odd number.

odd_number = 0
print(no_list)
for j in range(0, len(no_list)-1):
    if no_list[j] == 0:
        for i in no_list[j:]:
            if i % 2 == 1 and i > odd_number:
                odd_number = i
        no_list.pop(j)
        no_list.insert(j, odd_number)
        odd_number = 0
print(no_list)












