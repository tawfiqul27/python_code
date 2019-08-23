# Make a two-player Rock-Paper-Scissors game.
#(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, 
# and ask if the players want to start a new game)

# Remember the rules:

#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock


print('Please enter r for rock, s for scissors, and p for paper')
a = input('Enter the input from player 1: ')

b = input('Enter the input from player 2: ')

if a == 'r' and b == 's':
    print('Player 1 is the winner. Congratulations !!!!!!!!! ')
elif a == 's' and b == 'r':
    print('Player 2 is the winner. Congratulations !!!!!!!!! ')
elif a == 's' and b == 'p':
    print('Player 1 is the winner. Congratulations !!!!!!!!! ')
elif a == 'p' and b == 's':
    print('Player 2 is the winner. Congratulations !!!!!!!!! ')
elif a == 'p' and b == 'r':
    print('Player 1 is the winner. Congratulations !!!!!!!!! ')
else:
    print('Player 2 is the winner. Congratulations !!!!!!!!! ')








