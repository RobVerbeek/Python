#
colour = input("What is your favorite colour: ")

#seperate the first and third character
print(colour[0] + colour[2])
print("length = " + str(len(colour)))

print()

for i in range(len(colour)):
    print(colour[i] + " = ", str(ord(colour[i])))

for char in colour:
    print(char + " = ", str(ord(colour[i])))

j = 0
while j < len(colour):
    if j % 2 == 0:
        print("#",colour[j], "#")
    else:
        print("**", colour[j], "**")
    j += 1