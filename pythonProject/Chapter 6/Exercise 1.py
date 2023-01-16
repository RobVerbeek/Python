 # Write a function that returns the number of degrees Fahrenheit (Tf) when the temperature in degrees
# Celsius (Tc) is given as a parameter.  Use this conversion formula between Tc and Tf :

def conversion(Tf):
    Tc = Tf * 1.8 + 32
    return Tc
Tf = float(input("Enter a temperature in Celsius: "))
Tf = conversion(Tf)

print(Tf)