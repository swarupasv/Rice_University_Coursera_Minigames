# input will come from buttons and an input field
# all output for the game will be printed in the console

""" imporeted required modules """

import simplegui
import random

""" function new_game takes a parameter 100 0r 1000. 
100 for range[0,100) and 1000 for range[0,1000)"""

""" secret_number and count are global variables """
""" count varialble counts the number of guesses remaining """

# helper function to start and restart the game
def new_game(par):
    print "                          "
    print "*****NEW GAME*****"
    print "    "
    global secret_number
    global count
    if(par == 100):
        count = 7
        print "GUESS THE NUMBER FROM 0 UP TO 99"
        print "You have 7 guesses to win"
        print "                         "
        secret_number = random.randrange(0,100)
    else :
        count=10
        print "GUESS THE NUMBER FROM 0 UP TO 999"
        print "You have 10 guesses to win"
        print "                           "
        secret_number = random.randrange(0,1000)

""" two buttons for range 100 and range 1000 each.
Both call new_game function and pass parameter as 100 or 1000"""

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    new_game(100)	

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    new_game(1000)
    
""" input_guess takes the user input and compares it with the
secret_number. Though while loop is used to keep count of the remaining 
guesses, break statement is also used"""

def input_guess(guess):
    # main game logic goes here
    global count
    global secret_number
    print "Guess was "+str(guess)
    while(count > 1):
        guess=int(guess)
        if(guess == secret_number):
            print "Correct!"
            print "YOU WIN!"
            print "   "
            print "*****GAME OVER*****"
            new_game(100)
        elif(guess > secret_number):
            print "Guess a lower number than this"
        elif(guess < secret_number):
            print "Guess a higher number than this"
        count-=1
        print "you have "+str(count)+" guesses left"
        print "               "
        break
    else:
        print "YOU LOST!"
        print "   "
        print "*****GAME OVER*****"
        new_game(100)
    
    
# create frame
frame=simplegui.create_frame("GUESS THE NUMBER",300,300)

# register event handlers for control elements and start frame
frame.add_button("Range {0,100)",range100)
frame.add_button("Range {0,1000)",range1000)
frame.add_input("Guess",input_guess,200)
frame.start()

# call new_game 
new_game(100)


# always remember to check your completed program against the grading rubric
