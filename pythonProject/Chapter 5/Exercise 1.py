# Write a program to change the first and last element in a given (hard coded) list of strings. Print the
# List before and after the switch.

original_list = ['cat', 'dog', 'mouse', 'rat', 'squirrel', 'owl', 'rabbit']

print(original_list)
original_list = original_list[-1:] + original_list[1:-1] + original_list[:1]
print(original_list)
