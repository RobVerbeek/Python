#elf,me Rock = A, X 1 paper = B,Y 2 scissors = C, Z 3
score = 0
with open("Advent of code\day2\input.txt") as file:
    for line in file:
        elf, me = line.rstrip().split(" ")
        if me == "X": # Rock outcomes
            score += 1  
            if elf == "A":
                score += 3
            if elf == "C":
                score  += 6
        if me == "Y": #Paper outcomes
            score += 2
            if elf == "A":
                score += 6
            if elf == "B":
                score += 3
        if me == "Z": #scissor outcomes
            score += 3
            if elf == "B":
                score += 6
            if elf == "C":
                score += 3
    print(score)
#part 2
#elf,me Rock = A, X 1 paper = B,Y 2 scissors = C, Z 3
# X= lose Y= draw Z= win
score = 0
with open("Advent of code\day2\input.txt") as file:
    for line in file:
        elf, me = line.rstrip().split(" ")
        if me == "X": #lose  
            if elf == "A":
                score += 3
            if elf == "B":
                score += 1
            if elf == "C":
                score  += 2
        if me == "Y": #draw
            score += 3
            if elf == "A":
                score += 1
            if elf == "B":
                score += 2
            if elf == "C":
                score += 3
        if me == "Z": #win
            score += 6
            if elf == "A":
                score+= 2
            if elf == "B":
                score += 3
            if elf == "C":
                score += 1
    print(score)
