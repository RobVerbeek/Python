def control(choice):
    namelist = []
    attendance = []
    for line in file:
        record = line.rstrip().split(";")
        if record[-1] == choice:
            namelist.append(record[1:3])
    for i in namelist:
        name = i[0] + " " + i[1]
        present = input(f"{name}:")
        if present.upper() == "N":
            attendance.append(i + ["NOT"])
        else:
            attendance.append(i + ["OK"])
    return(attendance)
    
def classlist():
    classes = set()
    for line in file:
        record = line.rstrip().split(";")
        classes.add(record[3])
    return(classes)

with open("Files for Chapter 12\classlist.csv") as file:   
    classes = classlist()
    print("Pick one of these classes:")
    for i in classes:
        print(i, end=" | ")
    print("")
with open("Files for Chapter 12\classlist.csv") as file:  
    choice = input("enter a classroom: ")
    attendance = control(choice)
    print(attendance)
if len(attendance) > 0:
    file = open(f"{choice}.txt", "w")
    for i in attendance:
        file.write(f"{i[0]};{i[1]};{i[2]}\n")
else:
    print("This class doesn't exist")