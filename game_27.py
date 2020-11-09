#!/usr/local/bin/python3

def game_27(type):
    print('''The aim of the game:
    Start on 27, 3 darts at each double starting at 1 and going up 1 each time.
    If you dont get any in the given double, take away the double value from 27.
    If you hit the double, add on the value as many times as you hit it.''')
    score = type
    double = 1
    while score > 0:
        print('\n\tYou are currently on:', score)
        print('\tAim for Double', double)
        dart = int(input('\tHow many doubles did you hit?\t'))
        if dart > 3:
            print('You can only throw 3 darts per go!!')
            continue
        if 0 < dart < 4:
            score = score + (double * 2 * dart)
            double += 1
        if double == 21 and score > 0:
            double += 4
            print('Almost Won!! Now aim for the outer bull!!')
        if double == 25 and score > 0:
            doule = 50
            print('Just Bullseye to go. Take Aim!')
            dart = int(input('How many did you get?'))
            if dart > 3:
                print('You can only throw 3 darts per go!!')
                continue
            if 0 < dart < 4:
                score = score + (double * 2 * dart)
                double += 1
            elif dart == 0:
                score = score - (double * 2)
                double += 1
            if score > 0:
                print('You have won!! Finished with a score of:', score)
            else:
                if score < 0:
                    print('Almost got there just 1 Bullseye away')
        elif dart == 0:
            score = score - (double * 2)
            double += 1
    else:
        if score <= 0:
            print('\tYou have lost, well done though, you managed to get to: Double', double)
            again = input('Would you like to play again? (y/n)\t')
            if again == 'y':
                new_type = input('New game type: (y/n)\t')
                if new_type == 'y':
                    game_type()
                if new_type == 'n':
                    type = 27
                    game_27(type)
            if again == 'n':
                print('All Done, Come play again soon!!')
                exit()

type = 27
game_27(type)
