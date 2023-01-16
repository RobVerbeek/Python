# Write a program to read a string and form a new string. The characters are changed into groups of 3.
# If there was abc in the original string, it will be bca in the new string.
# This process is repeated for all subsequent groups of 3. The last remaining (1 or 2) letters are simply
# added.
input_string = input("Enter a string: ")
string = ""
for i in range(0, len(input_string), 3):
    if (i + 2) < len(input_string):
        split_string = input_string[i:i+3]
        string += split_string[1] + split_string[2] + split_string[0]
    else:
        split_string = input_string[i:len(input_string)]
        string += split_string
print(string)





