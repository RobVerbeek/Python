year = int(input("Enter a year: "))


if year % 4 == 0:
    if year < 1582:
        print(f"{year} is a leap year")
    else:
        if year % 400 == 0 and year % 4000!= 0:
            print(f"{year} is a leap year")
        elif year % 100 == 0 or year % 4000 == 0:
            print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
        
