months = {'January': 30,
          'February': 28,
          'March': 30,
          'April': 31,
          'May': 30,
          'June': 31,
          'July': 30,
          'August': 31,
          'September': 30,
          'October': 31,
          'November': 30,
          'December': 31}

poop = input("Enter a month: ")
poop = poop.capitalize()
if poop not in months:
    print("This month does not exist")
else:
    if poop == "":
        for i in months:
            print(i, months.get(i))
    else:
        print(months.get(poop))
