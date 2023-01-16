from random import randint

tile1 = randint(20, 40)
tile2 = randint(20, 40)
# loop until someone wins
while tile1 > 0 and tile2 > 0:
    choice = int(input("From which pile do you take?: "))
    amount = int(input("How many matches (between 3 and 8) do you want to take?: "))
    #check tiles and substract amount
    if 3<= amount <=8:
        if choice == 1:
            tile1 -= amount
            print(tile1)
        elif choice == 2:
            tile2 -= amount
            print(tile2)
        #computer choice
        if tile1 > 0 and tile2 > 0:
            pc_tile = randint(1, 2)
            pc_amount = randint(3, 8)
            if pc_tile == 1:
                tile1 = tile1 - pc_amount
            elif pc_tile == 2:
                tile2 = tile2 - pc_amount
            pc = True
        if tile1 <= 0 or tile2 <= 0:
            if pc == True:
                print("I win")
            else:
                print("congratulations")
        pc = False
    else:
        print("invalid amount, Please enter a valid amount")
