# Write a program to read a word and a number. Then print a new word consisting of the first
# character followed by the last 'number' of characters from the given word.
word = input("Enter a word: ")
number = int(input("Enter a number: "))

print(word[0] + word[-number:])