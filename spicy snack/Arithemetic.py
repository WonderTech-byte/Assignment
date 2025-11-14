first_number = int(input("Enter First Number: "))
second_number = int(input("Enter second Number: "))
third_number = int(input("Enter third Number: "))
min_number = 0
max_number = 0

sum_of_numbers = first_number + second_number + third_number
avarage = sum_of_numbers / 3
product = first_number * second_number * third_number

if first_number > second_number or first_number > third_number:
    print(f"the Largest Number is {first_number}")
    if second_number > first_number or second_number > third_number:
        print(f" the Largest Number is {second_number}")
        if third_number > first_number or third_number > second_number:
            print(f"the Largest Number is {third_number}")
