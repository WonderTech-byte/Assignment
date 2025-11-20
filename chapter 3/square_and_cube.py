print("number\tsquare\tcube")
for numbers in range(6):
    square = pow(numbers, 2)
    cube = pow(numbers, 3)
    print(f"{numbers:>5}\t{square:>5}\t{cube:>5}")
