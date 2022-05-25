# Author: SMR (AMDG) 05/17/22

import random
# Blank List for attempts
attempts_list = []

# Shows the previous score
def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, it's up for grabs!")
    else:
        print("The current high score is {} attempts, you got this!".format(min(attempts_list)))
# Starting the actual function of the game
def start_game():
    # Starts choosing the random number 1-100 inclusive
    rand_num = int(random.randint(1, 100))
    print("Hello newcomer! Welcome to Sean's Guessing Game!")
    
    # Prompt the user for their name and if they would like to play the game
    player_name = input("What is your name? ")
    wanna_play = input("Hello {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))
    ''' Where the show_score function USED to be'''
    
    # Count attempts
    attempts = 0
    show_score()
   
    # Actual Loop of the Game
    while wanna_play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 100 ")
            if int(guess) < 1 or int(guess) > 100:
                raise ValueError("Please guess a number within the given range")
            if int(guess) == rand_num:
                print("Nice! You guessed it!")
                attempts += 1
                attempts_list.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again = input("Would you like to play this game again? (Enter Yes/No) ")
                attempts = 0
                show_score()
                rand_num = int(random.randint(1, 100))
                if play_again.lower() == "no":
                    print("Wow ok, have a good one....")
                    break
            elif int(guess) > rand_num:
                print("It's lower")
                attempts += 1
            elif int(guess) < rand_num:
                print("It's higher")
                attempts += 1
        except ValueError as error:
            print(" This is not a valid value. Try again...")
            print("({})".format(error))
    else:
        print("That's cool, have a good one!")
if __name__ == '__main__':
    start_game()