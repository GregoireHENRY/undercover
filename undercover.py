import sys
import os
import random


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
    if win == 1:
        print('Civilian win')
    elif win == 2:
        print('Mr White & Undercover win')
    elif win == 3:
        print('Undercover wins')
    elif win == 4:
        print('Mr White wins')


def round_start_random(names, roles):
    print('Players: ', end='')
    for name in names:
        print('%s ' % name, end='')
    print()
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
        vote = input('Voter pour éliminter : ')
        try:
            vote = names.index(vote)
        except Exception as e:
            print(e, file=sys.stderr)
        else:
            break
    return vote


def eliminate(roles, names, vote, word):
    win = 0
    print('%s was %s' % (names[vote], roles[vote]))
    if roles[vote] == 'mrwhite':
        guess = input('Mr White devine le mot des civils avant de mourir : ')
        if guess == word:
            win = 3
    if not win:
        roles.pop(vote)
        names.pop(vote)
    return win


words = {
    'paix': 'amour',
    'escalator': 'ascenseur',
    'frambroise': 'cerise',
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
    print('%s est %s.' % (names[i], roles[i]))
    if roles[i] == 'civil':
        print('Word: %s.' % word[0])
    elif roles[i] == 'undercover':
        print('Word: %s.' % word[1])
    input()
    os.system('clear')

while True:
    round_start_random(names, roles)
    vote = proceed_vote(names)
    win = eliminate(roles, names, vote, word[0])
    win = win_condition(win, roles)
    input()
    os.system('clear')
    if win:
        break

win_message(win)

print()
print(word)
print(names)
print(roles)
