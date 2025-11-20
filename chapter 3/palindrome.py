number = int(input("Enter any number: "))
reverse_number =0 
new_number = number

while new_number != 0:
    last_digit = new_number % 10
    reverse_number = reverse_number * 10 + last_digit
    new_number = new_number // 10

if reverse_number != number:
    print(f"{reverse_number} is not a palindrome ")   
else: print(f"{number} is a palindrome")


