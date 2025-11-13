first_score = int(input("Enter first score: "))
second_score = int(input("Enter second score: "))
third_score = int(input("Enter third score: "))

average_score = (first_score + second_score + third_score) / 3
if average_score <= 60:
    print("F")
elif average_score > 60 and average_score <=70:
    print("D")
elif average_score >70 and average_score <= 80:
    print("C")
elif average_score > 80 and average_score <=90:
    print("B")
elif average_score > 90 and average_score <= 100:
    print("A")
