#!/usr/local/bin/python3
from collections import defaultdict
# d = defaultdict(int)

# d = {}

# players = raw_input('How many players?')
# players = int(players)

# for i in range (1,players+1):
  # d = raw_input('Enter player name')



players = ('james', 'jack', 'milky')

def game_multiple(score, *args):
    print('the number of players', len(*args), 'playing', score)

game_multiple(501, players)
