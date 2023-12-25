import random

def playGame():
    random_number = random.randint(1, 3)
    
    my_guess = input('Your guess: ')
    
    comp_move = ''
    
    result = ''
    
    if random_number == 1:
        comp_move = 'rock'
    elif random_number == 2:
        comp_move = 'paper'
    else:
        comp_move = 'scissors'

    if my_guess == 'rock':
        if comp_move == 'rock':
            result = 'You tie'
        elif comp_move == 'paper':
            result = 'You lose'
        elif comp_move == 'scissors':
            result = 'You win'
        else:
            print('Input a valid move')
    elif my_guess == 'paper':
        if comp_move == 'rock':
            result = 'You win'
        elif comp_move == 'paper':
            result = 'You tie'
        elif comp_move == 'scissors':
            result = 'You lose'
        else:
            print('Input a valid move')
    elif my_guess == 'scissors':
        if comp_move == 'rock':
            result = 'You lose'
        elif comp_move == 'paper':
            result = 'You win'
        elif comp_move == 'scissors':
            result = 'You tie'
        else:
            print('Input a valid move')
    else:
        print('input a valid move')
    print(f'You chose {my_guess}, computer chose {comp_move}. {result}')
playGame()

