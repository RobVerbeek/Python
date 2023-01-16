# Write a program to read a piece of text and save the characters (except spaces) in a List. Then
# print the List in three different ways.

sentence = input("Enter a sentence: ")

new_list = []

for i in sentence:
    if i != ' ' and i not in new_list:
        new_list += i
new_list.sort()
for i in new_list:
    print(i + " ", end=" ")
print()
print(new_list)
print(*new_list)

