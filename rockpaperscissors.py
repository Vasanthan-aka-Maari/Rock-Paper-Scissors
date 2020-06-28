
from random import randint as rn
l = ['rock' , 'paper' , 'scissors']

ai = l[rn(0,2)]

player = False

while player == False:
    player = input(' CHOOSE ANY ONE [rock , paper ,scissors] : ')
    if ai ==  'rock':
        if player == 'scissors':
            print('You lose ' , ai , 'smashed ' , player)
        elif player == ai:
            print('TIE')
        else:
            print('You win! ' , player , 'covered' , ai)

    elif ai == 'paper':
        if player == 'rock':
            print('You lose ' , ai , 'covered ' , player)
        elif player == ai:
            print('TIE')
        else:
            print('You win! ', player , 'smashed' , ai)

    elif ai == 'scissors':
        if player == 'paper':
            print('You lose ' , ai , 'cut' , player)
        elif player == ai:
            print('TIE')
        else:
            print('You win! ' , player , 'covered' , ai)

    rerun = input('If you want to continue(y/n) : ')
    if rerun == 'y':

        player = False
    else:
        print('THANK YOU. BYE BYE.')
        player = True
    
    ai = l[rn(0,2)]


        



