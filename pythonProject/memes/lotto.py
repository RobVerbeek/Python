from random import randint


def pick_lotto_balls(amount):
    new_list = []
    for i in range(amount+1):
        random = randint(1, 20)
        if new_list.count(random) < 1:
            new_list.append(random)
        else:
            amount - 1

    new_list.sort()
    return new_list



amount = int(input("How many balls would you like to pick?: "))
list = pick_lotto_balls(amount)
print("Guess 5 numbers")
correct = 0
for i in range(5):
    print("Guess: ", i+1, end="")
    guess = int(input(": "))
    if list.count(guess) == 1:
        correct += 1
if correct > 0:
    print("Number of correct answers :", correct)
else:
    print("No correct answers try again :-)")
print(list)

