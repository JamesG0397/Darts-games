#!/usr/local/bin/python3
def checkout(score):
    for line in open("checkouts_file", "r"):
        check = line.split()
        checkout = {}
        checkout[int(check[0])] = check[1:]
        if score in checkout.keys():
            print('Get these to checkout:\t', ', '.join(checkout[score]))

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

type = 121
game_121(type)
