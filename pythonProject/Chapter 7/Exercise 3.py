file = open("C:\\Users\\robve.LAPTOP-PCBR1UJF\\Downloads\\Files Chapter 7\\first_names.txt")
names = file.readlines()
count = 0
for i in names:
    count += 1
    print(i.ljust(13), end='')
    if count % 10 == 0:
        print()