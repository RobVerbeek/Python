def memer(line):
    count = 0
    memes = set()
    while line:
        memes.add(line)
        line = file.readline().rstrip()
    for i in memes:
        count += 1
    return([memes,count])
with open ("Files Chapter 10\\first_names1ITF.txt") as file:
    line = file.readline().rstrip()
    itf1, count1 = memer(line)
with open("Files Chapter 10\\first_names2ITF.txt") as file:
    line = file.readline().rstrip()
    itf2, count2 = memer(line)
unique = itf1.intersection(itf2)
count = 0
print(f"In ITF1 there are {count1} different first names")
print(f"In ITF2 there are {count2} different first names")
for i in unique:
    count += 1
print(count)
for i in sorted(unique):
    print(i)


