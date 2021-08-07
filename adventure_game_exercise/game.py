# Requirements:
#   - Write a short adventure game with no loops using only if and elif or else
#   - Accepts a choice at each step and moves the player to a choice of scenes

import random
import time

# This procedure displays the message passed and prompts the user that the game is over. 
# Asks if user want to restart game.
# Parameters:-
#   optional: 
#       1. message (can be any type) - message to be displayed
def endgame(message=''):
    print(message)
    choice = input("------GAME OVER! RESTART?-----\n(Y/N):")

    if(choice == 'Y' or choice == 'y'):
        run_game()
    else:
        # end the game 
        run_game(False)


# This procedure simulates a loading animation.
# Recursion was used instead of loop to fulfill the requirements of this exercise
# Parameters:-
#     mandatory: 
#       1. loop (int) - number of times to display '...' 
def loading(loop):
    if(loop <= 0):
        return
   
    time.sleep(0.5)
    print("... ")
    time.sleep(0.5)

    loading(loop - 1)

# Simulates a dice roll.
# Parameters:-
#     mandatory: 
#       1. level (str) - either 'easy' or 'hard'
# Output:-
#       return (int) - a random generated int
def dice_roll(level):

    result = ''
    value = 0

    # generate a random number between 1-5
    # if level is easy, you will win when the number generated is 3 or below
    # if level is hard, you will win when the number generated is 2 or below

    if(level == 'easy'):
        value = random.randint(1,5)
        
        if(value <= 3):
            result = 'WIN'
        else:
            result = 'LOSE'
    
    elif(level == 'hard'):
        value = random.randint(1,5)
        if(value <= 2):
            result = 'WIN'
        else:
            result = 'LOSE'
    
    # call loading procedure to add a bit of suspends during the dice roll
    loading(3)
    print(f'\nDice roll:{value} from 5\n')
    loading(3)

    return result

# When the player wins using this option which is harder, display a different message when won.
def option1():
    result = dice_roll('hard')

    if(result == 'WIN'):
        endgame("YOU WERE ADVENTUROUS AND YOU'VE OVERCOME THE ODDS! CONGRATULATIONS! YOU WON!")
    else:
        endgame("You were defeated in battle..")
    
# Display a simple message using the engame function when the player wins.
def option2():
    result = dice_roll('easy')

    if(result == 'WIN'):
        endgame("CONGRATULATIONS! YOU WON!")
    else:
        endgame("You got POISOINED")

# Parameters:-
#   Mandatory:
#       1. Options (list) - The 
#       2. Location (str) -
def route_two(options, location):
    
    print(f'\nYou\'re in the {location}.. What you want to do?')

    # print the options using recursions.
    # This is a nested function
    # Parametes:-
    #   mandatory:
    #       1. options - contains the list of data to be displayed
    #   optional: 
    #       1. i - the index indicating the current position in the list
    def show_options(options, i=0):
        if(i< len(options)):
            print(f"{options[i][0]} - {options[i][1]}")
            i += 1
            show_options(options,i)
    
    show_options(options)

    choice = input("Your choice: ")
    
    # Call the functions stored in the list based on the choice
    if(choice == '1'):
        cmd = options[0][2]
    elif(choice == '2'):
        cmd = options[1][2]
    else:
        run_game()
    
    cmd()

if __name__ == "__main__":
    
    # as long as game_on is True, run the function
    def run_game(game_on=True):

        # end the game
        if(game_on != True):
            return

        print('\nYou are at the forest, you can go left to the mountains, Right to the castle, Which way do you want to go?')
        print('1. Left.. to the mountains')
        print('2. Right.. to the Castle')
        print('3. Exit')

        choice = input('Your choice:')

        options = []

        # Depending on the choice, create the options for the following scene and proceed to the next scene
        if(choice == '1'):
            options = [(1,"Fight dragons", option1),
                        (2, "Eat berries", option2), 
                        (3, "Return", run_game)]
            route_two(options, 'mountains')
        elif (choice == '2'):
            options = [(1,"Conquer the Castle", option1),\
                        (2, "Have a feast with the King!", option2),
                        (3, "Return", run_game)]
            route_two(options, 'castle')
        elif (choice == '3'):
            loading(2)
            print('Thanks for playing!')
            return
        else:
            print("\nInvalid choice!\n")
            run_game()

    run_game()
    