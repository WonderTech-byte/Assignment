player1 = input("Enter your game 'rock: paper: scissors': ")
player2 = input("Enter your game 'rock: paper: scissors': ")



if player1 == "rock" and player2 == "scissors":
    print("player 1 wins")
    if player1 == "scissors" and player2 == "rock":
        print("player 2 wins")

if player1 == "paper" and player2 == "rock":
    print("player 1 wins")
    if player1 == "rock" and player2 == "paper":
        print("player 2 wins")

if player1 == "scissors" and player2 == "rock":
    print("player 2 wins")
    if player1 == "rock" and player2 == "scissors":
        print("player 1 wins")

if player1 == player2:
    print("its a tie")
