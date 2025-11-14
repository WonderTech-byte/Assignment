first_number = int(input("Enter First Number: "))
operator = input("Enter operator: ")
second_number = int(input("Enter second Number: "))

if operator == '+':
    sum_of_numbers = first_number + second_number
    print(f" sum of {first_number} is {sum_of_numbers}")
elif operator == '-':
    sum_of_numbers = first_number - second_number
    print(f" sum of {first_number} is {sum_of_numbers}")
elif operator == '/':
    sum_of_numbers = first_number / second_number
    print(f" sum of {first_number} is {sum_of_numbers}")
else:
    print("Enter valid number")
