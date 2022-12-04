from random import randint
# define variables
colourlist = ["R", "G", "B", "W"]
new_colourlist = []
initial_list = []
count = 1
correct = 0

# random colour picking function
def generate_random_colours():
    for i in range(0, amount):
        colour = randint(0, 3)
        new_colourlist.append(colourlist[colour])
    return new_colourlist


amount = int(input("How many colours would you like to guess?: "))
generate_random_colours()
guess = ""
# generate hidden colour list
for i in range(0, amount):
    initial_list.append("X")
    # edit the list if the guess is correct
for i in range(0, amount):
    guess = guess.capitalize()
    if guess == new_colourlist[count-1]:
        initial_list[count-1] = new_colourlist[count-1]
        correct += 1
    count += 1
    guess = input(f"Colour {count-1}?: ")
    print(initial_list)
print(f"Correct colours: {correct}") 