number = int(input("Enter any number: "))

while number > 0:
    last_digit = number % 10
    number = number // 10
    print(last_digit, end= " ")  
#print()
    
