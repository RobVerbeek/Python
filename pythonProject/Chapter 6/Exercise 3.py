def press_square(number, character):
    for i in range(number):
        print(character * number)


character = input("Enter a character, to stop press enter: ")
while character != "":
    number = int(input("amount of characters per line = amount of lines: "))
    press_square(number, character)
    character = input("Enter a character, to stop press enter: ")


