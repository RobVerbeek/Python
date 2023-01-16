stacks = [ 
["Z","N"],
["M","C","D"],
["P"]
]
newstacks = [ 
["Z","N"],
["M","C","D"],
["P"]
]

with open("Advent of code\day5\\test.txt") as file:
    for line in file:
        move = [] # 0 crates |1 from stack | 2 to stack
        for char in line:
            if char.isdigit():
                move.append(char)
        print(move)
        for i in range(int(move[0])):
            for i in stacks[int(move[1])-1]:
                count = 0
                if count <= int(move[0]):
                    newstacks[int(move[2])].append(i)
                    newstacks[int(move[1])].pop()
                    count += 1
                    print(newstacks)


