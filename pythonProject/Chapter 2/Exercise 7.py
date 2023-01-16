# select the bigger of 2 numbers unless dividable by 5 then choose the smaller number
n1 = int(input("The first number: "))
n2 = int(input("The second number: "))
#
if n1 < 0:
    n1 = n1 * (-1)
if n2 < 0:
    n2 = n2 * (-1)
#
if n1 % 5 == 0 and n2 % 5 == 0:
    if n1 < n2:
        print("The answer for the numbers", n1, "and", n2, "is:", n1)
    if n1 > n2:
        print("The answer for the numbers", n1, "and", n2, "is:", n2)
elif n1 % 5 >= 0 or n2 % 5 >= 0:
    if n1 > n2:
        print("The answer for the numbers", n1, "and", n2, "is:", n1)
    if n1 < n2:
        print("The answer for the numbers", n1, "and", n2, "is:", n2)
