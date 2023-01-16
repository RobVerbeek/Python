word = input("Enter a word: ")
ignore = input("Enter a letter to ignore: ")
#A -> a = +32
count = 0
new_word = ""
for letter in word:
    if ord(letter) >= ord("A") and ord(letter) <= ord("Z"):
        letter = ord(letter) + 32
        letter = chr(letter)
    if ord(ignore) >= ord("A") and ord(ignore) <= ord("Z"):
        ignore = ord(ignore) + 32
        ignore = chr(ignore)
    if letter == ignore:
        new_letter = ignore
        count += 1
    else:
        new_letter = "+"
    new_word += new_letter

print(new_word)
if count > 1:
    print("The character",ignore, "was ignored", count, "times.")
elif count == 1:
    print("The character",ignore, "was ignored", count, "time.")
else:
    print("No characters were ignored.")


