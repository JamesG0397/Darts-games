#!/usr/local/bin/python3


def checkout(score):
    for line in open("checkouts_file", "r"):
        check = line.split()
        checkout = {}
        checkout[int(check[0])] = check[1:]
        if score in checkout.keys():
            print('Get these to checkout:\t', ', '.join(checkout[score]))

def game_type():
    print('These are the game types available:\n501     301     121     27')
    type = int(input('Which game type do you want to play??\t'))
    if type == 501:
        print('You have selected to play 501!')
        throws = 0
        game_501(type, throws)
    if type == 301:
        print('You have selected to play 301!')
        throws = 0
        game_501(type, throws)
    if type == 121:
        print('You have selected to play 121!')
        game_121(type)
    if type == 27:
        print('You have selected to play 27!')
        game_27(type)

def game_501(type, throws):
    # print('not completed yet')
    score = type
    x = throws
    while score > 0:
        print('Current score:\t'.strip(), score)
        if score < 170:
            print('You can now checkout!!')
            checkout(score)
        dart = int(input('What did you score?\t'))
        if dart > 180 or 171 <= dart <= 179:
            print("This score isn't possible!!")
            continue
        score = score - dart
        x += 1
        # print(x) test to see if average was working
        if score == 1 or score < 0:
            print('You have bust!!, Go to previous score!!')
            score = score + dart
    else:
        if score == 0:
            double = input('Did you checkout with a double? (y/n)\t')
            if double == 'y':
                x += 1
                Average = 501/x
                print('Congratulations you have checkout!!\n\t Your game average was:', round(Average, 2))
                again = input('Would you like to play again? (y/n)\t')
                if again == 'y':
                    new_type = input('New game type: (y/n)\t')
                    if new_type == 'y':
                        game_type()
                    if new_type == 'n':
                        throws = 0
                        game_501(type, throws)
                if again == 'n':
                    print('All Done, Come play again soon!!')
                    exit()
            elif double == 'n':
                type = dart
                print(x)
                print('You have to finish on a double')
                throws = x
                game_501(type, throws)


def game_121(type):
    print('\nThe aim of this game is to checkout', type, 'in 9 darts.\nIf successful, increase the target by 1 and keep going!!!')
    score = type
    goes = 0
    while score > 0:
        print('\t')
        checkout(score)
        print('You need to get', score)
        print('Number of goes left =', 3 - goes)
        dart = int(input('What did you score?\t'))
        score = score - dart
        goes += 1
        if score < 0 or score == 1:
            print('You have gone bust! Start again!!')
            game_121(type)
        if score == 0 and goes <= 3:
            double = input('Did you checkout with a double? (y/n)\t')
            if double == 'y':
                print('Congratulations, you can now attempt to get', type + 1)
                next_level = input('Do you want to continue play on? (y/n)')
                if next_level == 'y':
                    type += 1
                    game_121(type)
                if next_level == 'n':
                    print('All Done, Come play again soon!!')
                    exit()
            elif double == 'n':
                print('You have to finish on a double! Start Again!')
                game_121(type)
        if goes >= 3 and score != 0:
            print('\nYou didnt get it this time, keep going!!')
            game_121(type)

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
        if double == 21:
            double = 25
            print('Almost Won!! Now aim for the outer bull!!')
            continue
        if double == 26:
            double = 50
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

game_type()
