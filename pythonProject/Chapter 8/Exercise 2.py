# student number surname name courses + student groups
with open ("Files chapter 8\\courses.csv") as file:
    line = file.readline().rstrip()
    record = line.split(";")
    while line:
        new_record = []
        nameind = record[4]
        new_record.append(record[3])
        for i in record[4:]:
            new_record.append(i)
        while line and record[4] == nameind:
            course = f"{record[1]} ({record[2]})"
            new_record.append(course)
            line = file.readline().rstrip()
            record = line.split(";")
        with open ("Files chapter 8\\compressedcourses", "a") as compressedcourses:
            for i in new_record:
                compressedcourses.write(i + ",")
            compressedcourses.write("\n")




