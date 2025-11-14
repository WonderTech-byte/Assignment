#declear and initialize first number
#declear and initialize second number
#check if first number is divisble by 4 without a remiander
#if first number is divisible without remainder, print fist number is a multiple of 4
#if first number not properly divisible, print not a multiple of 4
#check if second number is a multiple of 10
#if second number is properly divisble by 10 without remainder, print number is a multiple of 10
#if not print second number is not a multiple of 4


first_number = 1024
second_number = 2
if first_number % 4 == 0:
    print(f"{first_number} is a multiple of 4")
else: print(f"{first_number} is not a multiple of 4")

if second_number & 10 == 0:
    print(f"{second_number} is a multiple of 10")
else: print(f"{second_number} is not a multiple of 10")
