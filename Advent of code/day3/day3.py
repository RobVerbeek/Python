#part 1
#find common item
with open("Advent of code\day3\input.txt") as file:
    sum = 0
    for line in file:
        half1 = slice(0,len(line)//2)
        half2 = slice(len(line)//2, len(line))
        compartment1 = set(line[half1])
        compartment2 = set(line[half2])
        item = compartment1.intersection(compartment2)
        for i in item:
            item = str(i)
#calculate priority 
        if item >= "a" and item <= "z":
            priority = ord(item) -96
        if item >= "A" and item <= "Z":
            priority =ord(item) -38 
        sum += priority
    print(sum)
#part 2
with open("Advent of code\day3\input.txt") as file:
    sum = 0
    line = file.readline().rstrip()
    while line:
        g1 = set(line)
        g2 = set(file.readline().rstrip())
        g3 = set(file.readline().rstrip())
        badge = g1 & g2 & g3
        for i in badge:
            badge = str(i)
        if badge >= "a" and badge <= "z":
            priority = ord(badge) -96
        if badge >= "A" and badge <= "Z":
             priority =ord(badge) -38 
        sum += priority
        line = file.readline().rstrip()
    print(sum)








            
            



    



