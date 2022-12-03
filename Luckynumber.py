import random
import time
num = range(1,100)
num_choice = random.choice(num)
start = input('start the guessing game! y/n: ')
# condition to begin
if  start=='y' or start == 'yes':
    print('Welcome to LuckyGuess')
else:
    print('Goodbye')
    quit()
name = input('Enter your name: ').capitalize()
print('You have 4 chances to guess the lucky number')
time.sleep(1)
player_choice=None
for i in range(1, 5):
    #catch non interger Error msg
    try:
        player_choice=int(input(f'{name} Guess the lucky number in {num}: '))
        if player_choice > num_choice:
            print('your guess is high')
        elif player_choice < num_choice:
            print('your guess is low')
        else:
            print('you guessed right')
            break
    except:
        print('ValueError: you lost 1 Try, Enter a number')
        continue
#compare points - give result
if player_choice == num_choice:
    print(f'{name} YOU WON')
else:print(f'{name} YOU LOST')