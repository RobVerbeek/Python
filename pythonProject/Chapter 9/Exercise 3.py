with open("Files Chapter 10\\local_booking.txt") as file:
    line = file.readline().rstrip()
    record = line.split(";")
    classroom = set()
    while line:
        classroom.add(record[3])
        line = file.readline().rstrip()
        record = line.split(";")
    for i in classroom:
        print(i)

