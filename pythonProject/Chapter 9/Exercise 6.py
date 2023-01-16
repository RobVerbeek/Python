with open("Files Chapter 10\\food.txt") as file:
        line = file.readline()
        record = line.split(";")
        food = {}
        while line:
            food[record] = 1
            line = file.readline()
            record = line.split(";")

#food = {'Cows': 'moo',
#        'Cats': 'meow',
#        'Dogs': 'bark',
#        'Birds': 'whistle'}
meals = 0
for i in food:
        noise = input(f'What sound does {i} make?: ')
        if noise == food.get(i, 1):
                meals += 1
print(f'Correct answers: {meals}')