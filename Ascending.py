first_number = int(input("Enter First Number: "))
second_number = int(input("Enter Second Number: "))
third_number = int(input("Enter Third Number: "))

if first_number < second_number and first_number < third_number:
    if second_number < third_number:
        print(str(first_number), str(second_number), str(third_number))
    else: print(str(first_number), str(third_number), str(second_number))

if second_number < first_number and second_number < third_number:
    if first_number < third_number:
         print(str(second_number), str(first_number), str(third_number))

if third_number < first_number and third_number < second_number:
    if first_number < third_number:
         print(str(third_number), str(first_second), str(first_number))

