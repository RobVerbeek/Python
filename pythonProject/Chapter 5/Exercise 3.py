# In this program you use a List of animal names. Write the code to move the elements of the List one
# place to the left.
original_list = ['cat', 'dog', 'mouse', 'rat', 'squirrel', 'owl', 'rabbit']

print(original_list)
original_list = original_list[1:] + original_list[:1]
print(original_list)
