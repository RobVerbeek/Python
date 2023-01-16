count = 0
part2 = 0
pairs = []
with open("Advent of code\day4\\input.txt") as file:
    for line in file:
        elf1, elf2 = line.strip().split(",")
        pairs.append([elf1, elf2])
    for i in pairs:
        elf1 = i[0]
        elf2 = i[1]
        #range elf1
        half1,half2 = elf1.split("-")
        elf1range = list(range(int(half1), int(half2)+1))
        #range elf2
        half1,half2 = elf2.split("-")
        elf2range = list(range(int(half1), int(half2)+1))
        #compare
        if elf1range[0] <= elf2range[0] and elf1range[-1] >= elf2range[-1]:
            count += 1
        elif elf2range[0] <= elf1range[0] and elf2range[-1] >= elf1range[-1]:
            count += 1
        #part 2
        elfset1 = set(elf1range)
        elfset2 = set(elf2range)
        shared = elfset1 & elfset2
        if len(shared) > 0:
            part2 += 1
    print(count)
    print(part2)











    
    
      

