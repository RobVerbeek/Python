file = open("C:\\Users\\robve.LAPTOP-PCBR1UJF\\Downloads\\Files Chapter 7\\schedule.txt")
line = file.readline()
while line:
    if line != "\n":
        record = line.split(";")
        print(record[0], record[2].rstrip(), record[1], sep="\t")
    line = file.readline()
