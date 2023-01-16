# Write a program that allows the user to print the following series of integers, for each number
# between 10 and 20.
name = str(input("Name: "))
age = int(input("Age: "))
time = int(input("Member for how many years: "))
price_adult = 95
price_teen = 50
price_kid = 20
#
for i in range(1, 4+1):
    if age < 12:
        price = price_kid
    else:
        price = price_teen
    if age > 18:
        price = price_adult
    if time >= 5:
        price = float(price*0.9)
    print("Information for member", i)
    print("Name:",name, "\n", "Age: ", age, "\n", "Member for how many years: ", time, "\n", "Member fee for", name,":", price)
    if i < 4:
        name = str(input("Name: "))
        age = int(input("Age: "))
        time = int(input("Member for how many years: "))