binary = int(input("Enter decimal values(base 2): "))
number = binary
length = len(str(binary))
base = 2
decimal = 0
bin_conversion = 1
count = 0

for superscript in range(0, length, 1):
    power = base ** superscript
#    print(power)
    
    while binary > 0:
        each_digit = binary % 10
        binary = binary // 10  

    decimal = each_digit * power

    if count == 2: 
        print("decial here")
        print(decimal)
    

    count+= 1

  
#print(f"{number} in base 10 is {decimal}")
#print("  ", bin_conversion, end = " ")
    
#rint(count)   
    
