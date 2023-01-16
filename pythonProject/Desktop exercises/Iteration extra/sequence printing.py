limit = int(input("Up to which limit would you like to print the sequence of Fibonacci: "))
sequence = [0, 1]

if limit > 0:
    while sequence[-1] + sequence[-2] < limit:
        fibonacci = 0
        for i in sequence[-2:]:
            fibonacci = fibonacci + i
        sequence.append(fibonacci)
    print(sequence)
else:
    print("0")

