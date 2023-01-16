def read_books():
    books = file.readlines()
    return(books)

def print_list(books):
    count = 0
    for i in books:
        count += 1
        print(f"{count}. {i}")

def menu():
    print(" a - Overview\n b - Longest title\n c - 5 letters on a row\n s - Stop")
    choice = input("Make your choice: ")
    while choice.upper() not in ["A","B","C","S"]:
        print(" a - Overview\n b - Longest title\n c - 5 letters on a row\n s - Stop")
        choice = input("Make your choice: ")
    return(choice)  

with open("Files for Chapter 12\\books.txt") as file:
    choice = menu()
    books = read_books()
    if choice.upper() in ["A","B"]:
        print_list(books)
        if choice.upper() == "B":
            longest = 0
            for i in books:
                booklength = len(i)
                if booklength > longest:
                    longest = booklength
            print(f"The longest title has {longest} characters")
    if choice.upper() == "C":
        choice = int(input("Enter a booknumber max 10: "))
        book = books[choice-1]
        count = 0
        for i in book:
            print(i, end=" ")
            count += 1
            if count % 5 == 0:
                print("\n")
        
                



        





    