#This is a guess the number game
import random
print('Hello. What is your Name?')
name = input()

while True:
    secretNumber = random.randint(1,20)
    print('Well, ' + name + ', let us play a number game! \n')
    print('I am thinking of a number between 1 and 20 \n')

    #Ask the player to guess the number
    numGuesses = 0;
    while True:
        print('Take a guess or type in "G" to Give up.')
        try:
            guess = input()
            numGuesses = numGuesses + 1
            if int(guess) == secretNumber:
                print('Good Job, '+ name + '! You guessed my number in ' +str(numGuesses) + ' Guesses')
                break
            elif int(guess) > secretNumber:
                print('Your guess is Too High. \n')
            elif int(guess) < secretNumber:
                print('Your Guess is Too Low. \n')
        except:
            if(guess == 'G'):
                print('The number that I was thinking of was ' + str(secretNumber))
                break

    print('Do you want to play again \n')
    print('Enter any key for yes and "N" for no')
    playAgain = input();
    if(playAgain == 'N'):
        print('Thank you for playing! Have a great day!')
        break
        
        
    
    




    
