#A triple in a text is a character that occurs 3 times in a row. Write a program to count the number of
# triples in a text. The triples may overlap, as in the second example!
word = input("Enter a word: ")
count = 0
triples = 0
last_letter = word[0]

for letter in word:
    if last_letter == letter:
        count += 1
    if last_letter != letter:
        count = 0
    if count >= 2:
        triples += 1
    last_letter = letter
if triples >= 1:
    print(f"This word has {triples} triples.")
else:
    print("This text has no triples")



