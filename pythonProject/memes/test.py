from random import randint
amount = 20
new_list = []
for i in range(amount + 1):
    random = randint(1, 20)
    if new_list.count(random) < 1:
        new_list.append(random)
        new_list.sort()
print(new_list)
