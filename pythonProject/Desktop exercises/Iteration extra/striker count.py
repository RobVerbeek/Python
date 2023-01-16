count = 0

print("Press Enter for each new striker you see.\n If you want to pass a group, enter the number of strikers.\n If you want to stop, type S and press Enter.")
decision = ""

while decision != "Y" and decision != "y":
    striker = input (">> ")
    if striker == "S":
        print("Do you really want to stop Y/N? ")
        decision = input(">> ")
    elif striker != "":
        group = int(striker)
        count += group
    else:
        count += 1
print(f"Total number of strikers {count}")