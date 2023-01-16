def upperlower(sentence):
    count = 0
    bigcount = 0
    for i in sentence:
        if ord(i) >= 97 and ord(i) <= 122:
            count += 1
        if ord(i) >= 65 and ord(i) <= 90:
            bigcount += 1
    return (count, bigcount)


sentence = input("Enter a password with at least 2 capital letters and 3 lower letters: ")
# small, big = upperlower(sentence)
# print("Amount of small letters", small)
# print("Amount of capital letters",big)
small = 0
big = 0
while big < 2 and small < 3:
    small, big = upperlower(sentence)
    print("Requirements not met")
    sentence = input("Enter a password with at least 2 capital letters and 3 lower letters: ")


