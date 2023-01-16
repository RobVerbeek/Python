# Write a program that reads in your age and that of your father. Then calculate when your father is
# exactly twice as old as you.
my_age = int(input("How old are you: "))
dad_age = int(input("How old is your dad: "))
#
years = 0
if dad_age > my_age*2:
    while years + my_age*2 != dad_age:
        years += 1
        my_age_new = my_age + years
        dad_age_new = dad_age + years
    print("Within", years, "years your father will be double your age")
    print("I will be", my_age_new, "and my father will be", dad_age_new)
else:
    print("You're dad cannot be twice as old as you anymore")
