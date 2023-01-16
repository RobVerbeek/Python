with open ("Files chapter 8\\classrooms.txt") as file:
    line = file.readline().rstrip()
    record = line.split(";")
    while line:
        count = 0
        students = []
        roomind = record[2]
        while line and record[2] == roomind:
            name = record[0] + record[1]
            count += 1
            students.append(name)
            line = file.readline().rstrip()
            record = line.split(";")
        print(roomind)
        for i in students:
            print("\t", i)
        print(f"There are {count} number of students in {roomind}")

