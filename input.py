#!/usr/local/bin/python3

while True:
    print('''what game type would you like:
            501, 301, 27 or 121''')
    game_type = int(input('which one will it be?'))

    if game_type == 501:
        score = game_type
        print('your start score is:', score,'\n Throw your first 3 darts!')
        dart = int(input('you scored?\t'))
        if dart > 180:
            print('this score isnt possible!')
            score = score - dart
            print('you now have:', score, 'remaining')
            if score > 1:
                print(score, 'remaining. Throw again!!')
                dart = int(input('you scored?\t'))
                if dart > 180:
                    print('this score isnt possible!')
                    score = score - dart
