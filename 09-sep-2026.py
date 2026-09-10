# Rock, Paper, Scissors


# user vs computer
# ----------------
# rock vs paper - -> losses - - -> losses = losses + 1
# rock vs scissors - -> win ---> wins = wins + 1
# paper vs scissors - -> losses --> losses = losses + 1
# paper vs rock - -> win ---> wins = wins + 1
# scissors vs rock - -> losses --> losses = losses + 1
# scissors vs paper - -> win ---> wins = wins + 1
# usermove == computer_move - -> tie --> ties = ties + 1


# ROCK, PAPER, SCISSORS
# 0 Wins, 0 Losses, 0 Ties
# Enter your move: (r)ock (p)aper (s)cissors or (q)uit
# p
# PAPER versus...
# PAPER
# It is a tie!

# 0 Wins, 1 Losses, 1 Ties
# Enter your move: (r)ock (p)aper (s)cissors or (q)uit
# s
# SCISSORS versus...
# PAPER
# You win!

# GAME PROGRAM
import sys
import random


def rpsgame():
    print('ROCK, PAPER, SCISSORS')

    wins = 0
    losses = 0
    ties = 0

    while True:
        print(str(wins) + " Wins," + " " + str(losses) +
              " Losses," + " " + str(ties) + " Ties")

        # USER MOVE

        while True:
            print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')

            userMove = input()  # r

            if userMove == 'r':
                print('ROCK versus...')
                break
            elif userMove == 'p':
                print('PAPER versus...')
                break
            elif userMove == 's':
                print('SCISSORS versus...')
                break
            elif userMove == 'q':
                sys.exit()
            else:
                print('Invalid option! You must enter r,p,s or q')

        # COMPUTER MOVE

        computer_move = random.choice(['r', 'p', 's'])  # s

        if computer_move == 'r':
            print('ROCK')
        elif computer_move == 'p':
            print('PAPER')
        elif computer_move == 's':
            print('SCISSORS')

        # GAME LOGIC

        if userMove == 'r' and computer_move == 'p':
            print('You lost')
            losses = losses + 1
        elif userMove == 'r' and computer_move == 's':
            print('You win')
            wins = wins + 1
        elif userMove == 'p' and computer_move == 's':
            print('You lost')
            losses = losses + 1
        elif userMove == 'p' and computer_move == 'r':
            print('You win')
            wins = wins + 1
        elif userMove == 's' and computer_move == 'r':
            print('You lost')
            losses = losses + 1
        elif userMove == 's' and computer_move == 'p':
            print('You win')
            wins = wins + 1
        elif userMove == computer_move:
            print('It is a tie!')
            ties = ties + 1


rpsgame()
