import sys
import os
import random


class colors:
    NC = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    LIGHT_GRAY = '\033[37m'
    DARK_GRAY = '\033[90m'
    LIGHT_RED = '\033[91m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_MAGENTA = '\033[95m'
    BOLD = '\033[1m'
    BOLD = '\033[2m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    INVERTED = '\033[7m'
    HIDDEN = '\033[8m'


def create_roles_list(n_roles):
    roles = []
    for (key, value) in n_roles.items():
        for i in range(value):
            roles.append(key)
    return roles


def check_error_settings(names, roles):
    error = 0
    if len(names) != len(roles):
        error = 2
    if len(names) < 3:
        error = 3
    return error_message(error)


def error_message(error):
    if error == 1:
        sys.exit('Error in game settings')
    elif error == 2:
        sys.exit('Error in game settings: not same number of names and roles.')
    elif error == 3:
        sys.exit('Error in game settings: 3 players minimum.')


def win_message(win):
    print('%s%s%s' % (colors.BOLD, colors.BLINK, colors.LIGHT_YELLOW), end='')
    if win == 1:
        print('Civilian win!!')
    elif win == 2:
        print('Mr White & Undercover win!!')
    elif win == 3:
        print('Undercover wins!!')
    elif win == 4:
        print('Mr White wins!!')
    print(colors.NC, end='')


def round_start_random(names, roles):
    print('%sPlayers%s%s' % (colors.UNDERLINE, colors.NC, colors.LIGHT_GREEN),
          end='\n')
    for name in names:
        print('%s' % name)
    print(colors.NC)
    while True:
        start = random.randint(0, len(roles) - 1)
        if roles[start] != 'mrwhite':
            break
    print('%s starts to play!' % names[start])
    return start


def win_condition(win, roles):
    if win:
        return win
    win = 0
    if not roles.count('mrwhite') and not roles.count('undercover'):
        win = 1
    if roles.count('civil') == 1:
        if roles.count('mrwhite') or roles.count('undercover'):
            win = 2
            if not roles.count('mrwhite'):
                win = 3
            if not roles.count('undercover'):
                win = 4
    return win


def proceed_vote(names):
    while True:
        vote = input('%sVote to eliminate%s\n%s>%s %s' %
                     (colors.UNDERLINE, colors.NC, colors.BLINK, colors.NC,
                      colors.LIGHT_RED))
        print(colors.NC, end='')
        try:
            vote = names.index(vote)
        except Exception as e:
            print(colors.NC, end='')
            print(e, file=sys.stderr)
        else:
            break
    return vote


def eliminate(roles, names, vote, word):
    win = 0
    print('%s was %s' % (names[vote], roles[vote]))
    if roles[vote] == 'mrwhite':
        guess = input(
            '%sMr White guesses civilians\' word before dying%s\n%s>%s %s' %
            (colors.UNDERLINE, colors.NC, colors.BLINK, colors.NC,
             colors.LIGHT_MAGENTA))
        print(colors.NC, end='')
        if guess == word:
            win = 4
    if not win:
        roles.pop(vote)
        names.pop(vote)
    print(win)
    return win


words = {
    'paix': 'amour',
    'escalator': 'ascenseur',
    'framboise': 'cerise',
    'oiseau': 'papillon',
    'pikachu': 'chat',
    'zoo': 'aquarium'
}

n_roles = {'civil': 3, 'undercover': 1, 'mrwhite': 1}
names = ['Gregouze', 'Loulou', 'Adri', 'Sergio', 'Fabienne']
roles = create_roles_list(n_roles)

check_error_settings(names, roles)

random.shuffle(roles)
word = random.choice(list(words.items()))

os.system('clear')
for i in range(0, len(names)):
    print('%s%s%s is %s%s%s.' % (colors.LIGHT_GREEN, names[i], colors.NC,
                                 colors.LIGHT_GREEN, roles[i], colors.NC))
    if roles[i] == 'civil':
        print('Word: %s%s%s.' % (colors.LIGHT_MAGENTA, word[0], colors.NC))
    elif roles[i] == 'undercover':
        print('Word: %s.' % word[1])
    input()
    os.system('clear')

while True:
    round_start_random(names, roles)
    print(word)
    vote = proceed_vote(names)
    win = eliminate(roles, names, vote, word[0])
    win = win_condition(win, roles)
    input()
    os.system('clear')
    if win:
        break

win_message(win)
print()
print('%s%s%s' % (colors.LIGHT_MAGENTA, word, colors.NC))
print('%s%s%s' % (colors.LIGHT_GREEN, names, colors.NC))
print('%s%s%s' % (colors.LIGHT_GREEN, roles, colors.NC))
