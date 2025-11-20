
count = 1;
largest_number = 0
sum_of_number = 0
product = 1
smallest_number = 1000**10000

while count < 5:
    number = int(input("Enter number: "))   
    
    if number < smallest_number:
        smallest_number = number 

    if number > largest_number:
       largest_number = number
    
    sum_of_number += number
    product *= number
    count += 1


average = sum_of_number / 4







print(f" Smallest Number: {smallest_number}\n Largest Number: {largest_number}\n Sum of Numbers: {sum_of_number}\n Average: {average}\n Product: {product} ")
