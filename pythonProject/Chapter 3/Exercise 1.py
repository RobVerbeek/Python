#calculate a product
total = 1
count = 0
number = int(input("Enter a number, stop by entering 0: "))
#
while number != 0:
    count += 1
    total *= number
    number = int(input("Enter a number, stop by entering 0: "))
print("The product is:", total)