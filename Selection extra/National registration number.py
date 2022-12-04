name = "Jessica"#input("Enter your name: ")
firstgroup = int(input("enter the first 9 numbers of your national register number: "))
secondgroup = int(input("Enter the last 2 numbers of your national register number: "))

#check if the input is valid
while firstgroup // 100000000  <= 0 or firstgroup // 100000000 >= 10:
    print(f"Hello {name}, the national number you gave is not correct")
    firstgroup = int(input("enter the first 9 numbers of your national register number: "))

while secondgroup >= 100 or secondgroup < 10 or 97 - firstgroup % 97 != secondgroup:
    print(f"Hello {name}, the national number you gave is not correct")
    secondgroup = int(input("Enter the last 2 numbers of your national register number: "))
#gender selection
if firstgroup % 1000 %2 ==0:
    print(f"Hello {name}, your gender is female")
else:
    print(f"Hello {name}, your gender is male")
#print date of birth
print(f"You were born on {firstgroup //1000 %100}/{firstgroup // 100000 %100}/{firstgroup // 10000000}")




