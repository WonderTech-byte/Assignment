number_x = int(input("Enter first Number: "))
number_y = int(input("Enter second Number: "))

if number_x > 0 and number_y > 0:
    print("Q1")
if number_x < 0 and number_y > 0:
    print("Q2")
if number_x < 0 and number_y < 0:
    print("Q3")
if number_x > 0 and number_y < 0:
    print("Q4")
if number_y == 0 and number_x != 0:
    print("X-axis")
if number_x == 0 and number_y != 0:
    print("Y-axis")
