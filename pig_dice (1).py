#
#   The game of "pig"
#
#   The object of the game is to score as many points as possible.
#   You can either roll a die or keep your current total.
#   If you roll a 1, you lose. If you roll any other number, it is
#   added to your current score.
#

import random

#
#   This function will repeatedly ask you if you want to roll the die
#   or hold (keep your current total). If you enter 'r' or 'R', it will
#   return 'r' (for roll); if you enter 'h' or 'H', it will return 'h' (for
#   hold). If you enter any other string, the function gives an error message
#   and asks you for input again. Hint: use a while loop

def get_roll_or_hold():
    answer = input('R)oll or H)old? ')
    # your code goes here


#
#   This function will repeatedly ask you if you want to play again or not
#   If you enter 'y' or 'Y', it will return True; if you enter 'n' or 'N',
#   it will return False. If you enter any other string, the function gives
#   an error message and asks you for input again. Hint: use a while loop.

def play_again():
    answer = input('Play again? (Y/N) > ')
    # your code goes here
    


playing = True
print('Welcome to the game of "pig."')
      
while playing:

    total = 0
    rolling = True

    while rolling:
        # call get_roll_or_hold() and put return value into a variable named response
        # if the response is 'r':
        #   roll the die
        #   print the value of the roll
        #   if the die is 1:
        #     print a message that player lost this round
        #     set rolling to False
        #   else:
        #     add die value to total
        #     print current total
        # else:
        #   set rolling to False

    if response == 'h':
        # print total for the round, appropriately labeled

    print() # for spacing
    playing = play_again()  # will set playing to True or False

print('Thanks for playing the game.')
