# open file
file = open("C:\\Users\\robve.LAPTOP-PCBR1UJF\\Downloads\\Files Chapter 7\\first_names.txt")
count = 0
namez = 0
line = file.readline()
while line:
    count += 1
    if 'Z' in line or 'z' in line:
        namez += 1
    line = file.readline().rstrip()
file.close()
print(f"There are {count} names in the list")
print(f"There are {namez} names in the list containing the letter z")

