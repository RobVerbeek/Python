word= input("Enter a word: ")
if word.find('in') in (0,1):
    print("'in' appears in the first or second place")
elif word.find('in') == -1:
    print("This word does not contain 'in'")
else:
    print("'in' appears in the word, but not in the front")