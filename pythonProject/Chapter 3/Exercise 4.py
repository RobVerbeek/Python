# higher lower
number = 0
answer = 37
guesses = 0
#
while number != 37:
    guesses += 1
    number = int(input("Enter a positive number: "))
    if number < 37:
        print("Higher!")
    elif number > 37:
        print("Lower!")

print("You have guessed the number:",answer, "in", guesses, "guesses.")
