player1 = str(input("Player 1 is your turn(rock/paper/scissors): "))
player2 = str(input("Player 2 is your turn(rock/paper/scissors): "))

if (player1 == 'rock' and player2 =='rock') or (player1 == 'paper' and player2 == 'paper') or (player1 == 'scissors' and player2 == 'scissors'):
    print("Draw")

elif (player1 == 'rock' and player2 == 'scissors') or (player1 == 'paper' and player2 == 'rock') or (player1 == 'scissors' and player2 == 'paper'):
    print("Player 1 is winner")

elif (player1 == 'rock' and player2 == 'paper') or (player1 == 'paper' and player2 == 'scissors') or (player1 == 'scissors' and player2 == 'rock'):
    print("Player 2 is winner")  

else:
    print("There is not a choice like that")