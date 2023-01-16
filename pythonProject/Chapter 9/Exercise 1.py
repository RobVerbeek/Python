meme = input("Enter a text consisting of letters and numbers: ")
characters = set()
digits = set()
for i in meme:
    if i.isdigit():
        digits.add(i)
    else:
        characters.add(i)
print("The numbers: ")
for i in digits:
    print(i)
print("The characters: ")
for i in characters:
    print(i)




