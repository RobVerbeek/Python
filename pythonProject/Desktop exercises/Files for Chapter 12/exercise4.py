def lowest_price():
    with open("Files for Chapter 12\prices.txt") as file:
        prices = {}
        for line in file:
            item,price,place= line.rstrip().split(";")
            if item in prices:
                if prices[item] > price:
                    prices[item] = price
            else:
                prices[item] = price
        return(prices)

#main
prices = lowest_price()
print(prices)
print("Price list\n----------")
for i in prices:
    print(i, prices[i])
what = input("Enter the item (press x if you want to stop):")
while what.upper() != "X":
    if what in prices:
        print(f"The lowest price of {what} is {prices[what]}")
    else:
        print("This item is not available.")
    what = input("Enter the item (press x if you want to stop):")
    



            