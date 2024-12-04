import time
import random
print('Hlo!! There here i have build a game for u...')
print('Lets start..')
time.sleep(1)
print('Processing...')
time.sleep(2)
print('Follow the command and obey the rule...')

def guess(X):
    random_number = random.randint( 1 , X )
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess the number between 1 and {X} : '))
        time.sleep(2)
        if guess < random_number:
             print('sorry, guess again, too low')
        elif guess > random_number:
              print('sorry, guess again, too high')
        elif guess < random_number and guess > random_number:
             print('Are you confusee...')
        elif guess < random_number or guess > random_number:
             print('Are you confusee...')
    print(f' Congrats!! you guessed the right no. {random_number}...-_-')
guess(10)