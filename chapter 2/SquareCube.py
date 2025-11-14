#DISPLAYING THE SQUARE AND CUBE OF A NUMBER
#declare number in range of 0 to 6(printing 0 to 5)
#each number in range is then raise to the power of 2
#each number in range is alo raise to the power of 3
#each number in range is print out on the same line
print("number\tsquare\tcube")
for number in range(6):
    print(f"{number} \t {number ** 2} \t {number ** 3}")
