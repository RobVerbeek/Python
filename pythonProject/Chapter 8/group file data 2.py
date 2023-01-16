with open ("Files chapter 8\\classrooms.txt") as file:
    line = file.readline().rstrip()
    record = line.split(";")
    rooms = []
    while line:
        roomind = record[2]
        number = 0
        while line and record[2] == roomind:
            number += 1
            line = file.readline().rstrip()
            record = line.split(";")
        rooms.append([roomind, number])
    print(rooms)


