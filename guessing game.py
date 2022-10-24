import random
com_data = range(1, 11)
com_guess = None
plyer_guess = None
choice = 'yes'

def com():
    com_guess = random.choice(com_data)
    print('computer guess: '+ str(com_guess))
    return com_guess


def plyer():
    while True:
        plyer_guess = int(input('enter a number from 1 -> 10: '))
        if plyer_guess <= 10 and plyer_guess  >= 1 :
            print('you guessed : ' + str(plyer_guess))
            break
    return plyer_guess


def result():
    if plyer() == com():
        print('Your guess is same (YOU win)')
        print('GameOver')
    elif plyer() > com():
        print('Your guess is greater (YOU LOSE )')
        print('GameOver')
    elif plyer() < com():
        print('Your guess is lesser (YOU LOSE )')
        print('GameOver')
    else:
        'none'



def replay():

    plyr_choice = input('would you like to play again(yes / no)!!: ').lower()
    if plyr_choice == choice:
        result()
    else:
        print('Goodbye')








result()
replay()