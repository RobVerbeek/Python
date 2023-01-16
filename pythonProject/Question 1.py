# Rob Verbeek 1ACS02 r0932067
#ask for inputs
name = input("Enter your first name: ")
amount = int(input("Enter the number of characters you want to reverse: "))
reverse_name = "r"
# keep asking the amount until a 0 is entered
while amount != 0:
    #check if the inputs are correct or print an error
    if amount <= len(name) and amount > -1:
        new_name = name[:amount]
        reverse_name = new_name[::-1] + name[amount:]
        print(reverse_name)
    elif amount > len(name):
        print("The number of characters is too long")
    else:
        print("The number of characters must not be a negative number")
    amount = int(input("Enter the number of characters you want to reverse: "))

