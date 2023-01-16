with open ("Files chapter 8\\weather_2018 10.csv") as file:
    line = file.readline().rstrip()
    print(line)
    line = file.readline().rstrip()
    record = line.split(";")
    while line:
        date = record[0][0:10]
        temp = 0
        count = 0
        while line and record[0][0:10] == date:
            temp += float(record[1])
            count += 1
            line = file.readline().rstrip()
            record = line.split(";")
        average = temp / count
        print(date, round(average, 2), count)