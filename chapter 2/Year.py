year = int(input("Enter days in years : "))
if year % 4 == 0 or year % 400 == 0:
    print("its a leap year")
else: print("not a lead year")
