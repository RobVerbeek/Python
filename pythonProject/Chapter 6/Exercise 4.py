from random import randint


def generate_list(lower_limit, upper_limit):
    list1 = []
    for i in range(number):
        list1.append(randint(lower_limit, upper_limit))
    return list1


def filter1(dice):
    unique = []
    for i in dice:
        if not i in unique:
            unique.append(i)
    return unique



count = 0
lower_limit = 1
number = int(input("How many dice do you want to roll?: "))
upper_limit = int(input("How many sides does your dice have?: "))
dice = generate_list(lower_limit, upper_limit)
unique_dice = filter1(dice)
print(dice)
print("unique", unique_dice)
while dice.count(dice[0]) != number:
    count += 1
    dice = generate_list(lower_limit, upper_limit)
    print(dice)
print("Poker in: ", count)


