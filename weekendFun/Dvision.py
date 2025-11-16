first_number_x = int(input("Enter first number: "))
second_number_y = int(input("Enter second number: "))
if second_number_y != 0:
    quotient = first_number_x / second_number_y
    print(f"The quotient of {first_number_x} and {second_number_y} is {quotient}")
elif second_number_y == 0:
    print("cannot divide by zero")
