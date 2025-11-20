user_problem = input("what is your problem? ")
problem_occurence = input("Have you had this problem before(yes or no): ").lower()

if problem_occurence == "yes":
    print("well, you have it again")
elif problem_occurence == "no":
    print("Well, you have it now")
else: print("wrong input")


