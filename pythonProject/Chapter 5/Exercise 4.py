# Use a Tuple of at least 6 numbers in your program. Write the code to create a new Tuple containing
# all the numbers that appear after the last digit 4. Print the original Tuple and the new Tuple.

original_tuple = (1, 2, 3, 4, 5, 4, 6, 7, 8)
new_tuple = ()
lastfour = 0
for position in original_tuple[0:]:
    if original_tuple[position] == 4:
        lastfour = position + 1
new_tuple += original_tuple[lastfour:]

print(original_tuple)
print(new_tuple)


