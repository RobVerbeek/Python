file = open("C:\\Users\\robve.LAPTOP-PCBR1UJF\\Downloads\\Files Chapter 7\\first_names.txt")
line = file.readline().rstrip()
names = []
while line:
    names.append(line)
    line = file.readline().rstrip()
for i in names:
    print(i)
for i in names[::-1]:
    print(i)
