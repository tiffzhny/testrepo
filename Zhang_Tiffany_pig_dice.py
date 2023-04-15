# Tiffany Zhang
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
#   or hold (keep your current total). 

def get_roll_or_hold():
    answer = input('R)oll or H)old? ')
    answer = answer.lower()
    done = False
    while not done:
        if answer == "r":
            done = True 
            return answer
        if answer == "h":
            done = True
            return answer
        else:
            print("Please enter R to roll or H to hold.")
            answer = input('R)oll or H)old? ')
            answer = answer.lower()


#   This function will repeatedly ask you if you want to play again or not

def play_again():
    answer = input('Play again? (Y/N) > ')
    answer = answer.lower()
    finished = False
    while not finished:
        if answer == "y":
            finished = True
            return True
        if answer == "n":
            finished = True
            return False
        else:
            print("Please enter Y for yes or N for no")
            answer = input('Play again? (Y/N) > ')
            answer = answer.lower()
        

playing = True
print('Welcome to the game of "pig."')
      
while playing:

    total = 0
    rolling = True

    while rolling:
        response = get_roll_or_hold()
        if response == "r":
            value = random.randrange(1,7)
            print(f"You rolled a {value}")
            if value == 1:
                print("Sorry, you lost this round")
                rolling = False
            else:
                total = value + total
                print(f"Your total is {total}")
        else:
            rolling = False

    if response == 'h':
        print(f"Your total is {total}")

    print() # for spacing
    playing = play_again()  # will set playing to True or False
    
print('Thanks for playing the game.')
