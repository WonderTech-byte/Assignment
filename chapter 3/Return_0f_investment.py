#collect user investment returns, numbers of years and interest rate
#calculate the perentage rat
#calculate each of the ROI for each year by calculating each year in iteration



investment_amount = int(input("Enter investment amount: "))
numbers_of_years = int(input("Enter number of years: "))
interest_rate = float(input("Enter interest Rate: "))


print("year\tpercent\tROI")

for years in range(1, numbers_of_years+1):
    investment_amount += ((interest_rate/ 100)* investment_amount) 
    print(f" {years}\t{interest_rate}\t{investment_amount:.3f}")
   
    
    
    
    
    

