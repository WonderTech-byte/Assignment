pass_word = input("Enter password: ")
length = len(pass_word)
if length <= 1:
    print("Invalid Paaword")
elif length < 6:
    print("Password too Weak")
elif length > 6 and length < 10:
    print("Medium")
elif length > 10:
    print("Strong!!")
