# Write a function to convert an amount in Euro into Dollar. The function has 2 parameters: the amount in
# Euro and the exchange rate of the day. The function returns the amount in Dollar.

def conversion(euro):
    dollar = euro * 1.2327
    return dollar
euro = int(input("Euro's: "))
dollar = conversion(euro)
print(dollar)