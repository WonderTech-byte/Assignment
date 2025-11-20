number = int(input("Enter number to get factorial: "))
factorial = 1;

if number > 0:
    for numbers in range(1, number+ 1):
        factorial *= numbers
    print(f"Factorial of {number} is {factorial}")
else: print("Enter non negative integer")
