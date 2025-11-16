letter = input("Enter a letter: ")
if letter in ("a", "e", "i", "o", "u"):
    print("vowel")
elif letter.isdigit():
    print("invalid input")
else: print("Consonant")

