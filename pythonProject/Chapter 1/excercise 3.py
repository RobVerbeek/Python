#read 3 digit number
#data retrieval
#half double third power tenfold the digits are: x x x
number= input("Enter a 3 digit number: ")
#calculations
half= int(number/2)
double= int(number*2)
third_power= int(number**3)
tenfold= int(number*10)
#print
print("HALF = "+ str(half))
print("DOUBLE = "+ str(double))
print("THIRD POWER = "+str(third_power))
print('The digits are:')
first = number//100
second = (number % 100)//10
third = (number % 100) % 10
print(first)
print(second)
print(third)
