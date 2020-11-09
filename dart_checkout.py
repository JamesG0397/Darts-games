#!/usr/local/bin/python3


def checkout(score):
    for line in open("/Users/jamesgoodman/Desktop/Python/Dart_app/checkouts_file", "r"):
        check = line.split()
        checkout = {}
        checkout[int(check[0])] = check[1:]
        if score in checkout.keys():
            print('Get these to checkout:\t', ', '.join(checkout[score]))

score = 100
checkout(score)
