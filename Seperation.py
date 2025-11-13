number = int(input("Enter any five digit number: "))

first_number = number % 10
number = number // 10;
   
second_number = number % 10
number = number // 10;

third_number = number % 10
number = number // 10;

fourth_number = number % 10
number = number // 10;
    
last_number = number % 10
number = number // 10;

print(str(last_number),   str(fourth_number),   str(third_number),  str(second_number),     str(first_number))
    
