original = ['yellow', 'green', 'blue', 'purple']
encoded = []
def encoder(original, mirror_letter):
    for color in original:
        new_word = ""
        for letter in color:
            distance = ord(letter) - ord(mirror_letter)
            if distance < 0:
                distance *= -1
            if ord(mirror_letter) - distance < ord('a'):
                new_letter = ord(mirror_letter) - distance + 26
            elif ord(mirror_letter) + distance > ord('z'):
                new_letter = ord(mirror_letter) + distance - 26
            else:
                new_letter = ord(mirror_letter) - distance
            new_word += chr(new_letter)
        encoded.append(new_word)
    print("original:", original)
    print("encoded:", encoded)

start = ord('a')
for i in range(26):
    mirror_letter = chr(start + i)
    print(mirror_letter)
    encoder(original, mirror_letter)
    encoded = []


