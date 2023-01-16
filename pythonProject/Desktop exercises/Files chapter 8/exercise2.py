with open("Files chapter 8\courses.csv") as file:
    line = file.readline().rstrip()
    record = line.split(";")
    while line:
        newrecord = []
        name = record[4]
        for i in record[4:]:
            newrecord.append(i)
        while line and record[4] == name:
            course = f"{record[1]} ({record[2]})"
            newrecord.append(course)
            line = file.readline().rstrip()
            record = line.split(";")
        print(newrecord)
    

        
            