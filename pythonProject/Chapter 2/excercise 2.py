# if you are 18 years old or older you are an adult
birth_year = int(input('Enter your year of birth: '))
# calc
age = (2022-birth_year)
print('your age is:', age)
if age >= 18:
    print("you're an adult")
else:
    print("you're not an adult")