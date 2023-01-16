file = open("C:\\Users\\robve.LAPTOP-PCBR1UJF\\Downloads\\Files Chapter 7\\kilometers.txt")
line = file.readline().rstrip()
clowns = []
while line:
    number = int(line)
    clowns.append(number)
    line = file.readline().rstrip()
clowns.sort()
print(f"The difference between the largest and smallest number = {clowns[-1]} - {clowns[0]} = {clowns[-1] - clowns[0]}")
print(clowns)