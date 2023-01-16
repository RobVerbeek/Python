# Write a program that calculates the sum of all numbers between 25 and 32 (including the
# boundaries).
initial_limit = int(input("Initial limit: "))
final_limit = int(input("Final limit: "))
#
if initial_limit > final_limit:
    print("The initial limit must be lower than the final limit")
else:
    sum = initial_limit
    print("Sum of the numbers from", initial_limit, "Till", final_limit)
    if initial_limit == final_limit:
        print(sum)
    else:
        for counter in range(initial_limit+1, final_limit+1):
            sum += counter
            print("+", counter, "-->", sum)




