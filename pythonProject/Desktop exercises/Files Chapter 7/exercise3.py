with open("Files Chapter 7\\first_names.txt") as file:
    count = 0
    for line in file:
        count += 1
        print(line.rstrip().ljust(13), end="")
        if count % 10 == 0:
            print("")
        