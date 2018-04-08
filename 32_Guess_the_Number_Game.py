#Challenge included

import random

def difficulty(level):
    if level == 1:
        return random.randint(1,11)
    elif level == 2:
        return random.randint(1,101)
    elif level == 3:
        return random.randint(1,1000)


def comparison(guess, answer):
    if guess == answer:
        return 1
    elif guess < answer:
        return 2
    elif guess > answer:
        return 3

def rate(guess):
    if guess == 1:
        return 'You\'re a mind reader'
    elif 2<= guess <4:
        return 'Most Impressive'
    elif 4<= guess <= 6:
        return 'You can do better than that'
    else:
        return 'Better luck next time'

def trackanswer(newguess,oldguess):
    if newguess in oldguess:
        return True
    else:
        return False

def main():
    
    s1 = 'I have my number, What\'s your guess?'
    s2 = 'Too low. '
    s3 = 'Too high. '
    s4 = 'Guess again: '
    s5 = 'You\'ve guessed that number before'

    counter = 1
    answer = 0
    guess = 0
    trial = 0
    oldguess = []

    while True:
        try:
            level = int(input('Guess the Number Game Level(1,2 or 3):'))
            answer = difficulty(level)
        except ValueError:
            print('Choose a level')

    #Player's first guess                    
    while True:
        try:
            
            guess = int(input(s1))
            trial = comparison(guess, answer)
            oldguess.append(guess)
            break
        except ValueError:
            counter +=1
            print('This is not a number. ',s4)
 
    #If player's first guess is not correct, this part of code will excecute and continue the game
            
    while trial != 1:
        try:
            trial = comparison(guess, answer)
            
            if trial == 2:
                guess = int(input(s2+s4))
                counter +=1
                
                if trackanswer(guess, oldguess) == True:
                    print(s5)
                oldguess.append(guess)
                
            elif trial == 3:
                guess = int(input(s3+s4))
                counter +=1
                if trackanswer(guess, oldguess) == True:
                    print(s5)
                oldguess.append(guess)

   
        except ValueError:
            counter+=1
            print('This is not a number ',s4)

    print(f'You got it in {counter} guesses!')
    print(f'{rate(counter)}')
            


if __name__=='__main__':
    main()
    while True:
        again = input('Play again?:')
        if again =='y' or again == 'yes':
            main()
        else:
            print('Goodbye!')
            break
    
