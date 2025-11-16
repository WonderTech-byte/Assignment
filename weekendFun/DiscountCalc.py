total_bill = int(input("Enter your total bill: "))
is_member = input("Are you a member(Yes of No):")

if total_bill >= 100 and is_member == "yes":
    discount_calc = total_bill *(0.1)
    discounted = total_bill - discount_calc
    print(f"you have 10% off and final is {discounted}")
elif total_bill >= 1000 and total_bill != "yes":
    discount_calc = total_bill *(0.05)
    discounted = total_bill - discount_calc
    print("you have 5% off and final is {discounted}")
else: print(f"No discount and your final amount is {total_bill}")
