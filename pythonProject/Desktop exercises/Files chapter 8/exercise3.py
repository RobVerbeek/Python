with open("Files chapter 8\weather_2018 10.csv") as file:
    line = file.readline().rstrip()
    print(line)
    line = file.readline().rstrip()
    while line:
        record = line.split(";")
        date = record[0].split(" ")
        dateind = date[0]
        newdate = dateind
        count = 0
        temp = 0
        while line and dateind == newdate:
            count += 1
            temp += float(record[1])
            line = file.readline().rstrip()
            record = line.split(";")
            date = record[0].split(" ")
            newdate = date[0]
        print(count,dateind,round(temp/count,2))
