#Random number guessing game
#18 April 2018
#CTI-110 P5HW2 - Random Number Guessing Game
#Karla Weinbrenner

import random



def main():
    playAgain='y'
    while playAgain == 'y' or playAgain == 'Y':
       
        secretNumber = random.randint (1,100)
        guess = int(input("Enter a guess: "))
        while guess >0:
            if guess > secretNumber:
                print("The number is too high, try again ")
                guess = int(input("Enter a guess: "))
            elif guess < secretNumber:
                print("The number is too low, try again ")
                guess = int(input("Enter a guess: "))
            else:
                print("Correct! The number is ",secretNumber)
                guess = -1
                
        #play again?

        playAgain=input ("Play again? (y=yes): ")
            
main()
