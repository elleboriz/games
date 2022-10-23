import  random
dice_one = ['1', '2', '3', '4', '5', '6']
dice_two = ['1', '2', '3', '4', '5', '6']
com_dice = random.choice(dice_one)
plyr_dice = random.choice(dice_two)

#----------------------------
def com():
    for i in com_dice:
        value = int(i)
        print('com value: ', value)
        return value

        #print('com value: ',value)

def player():
    for i in plyr_dice:
        value = int(i)
        print('player value: ', value)

        return value


        #print('player value: ',value)

#----------------------------
def result():
    if com() > player() :
        print('computer Wins this round.')
    elif com() < player() :
        print('You Win this round.')
    elif com() == player() :
        print('this is a draw round.')
    else:
        None



result()