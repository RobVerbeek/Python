word = input("Enter a word: ")
count = 1
countl = 0
last_letter = word[0]

for letter in word:
    if last_letter == letter:
        count += 1
        if count > countl:
            countl += 1
    if last_letter != letter:
        count = 1
    last_letter = letter
print(f"The longest block in this string is {countl}")