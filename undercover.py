import sys
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
    return error_message(error)


def error_message(error):
    if error == 1:
        sys.exit("Error in game settings")
    elif error == 2:
        sys.exit("Error in game settings: not same number of names and roles.")


n_roles = {'civil': 3, 'undercover': 1, 'mrwhite': 1}
names = ["Gregouze", "Loulou", "Adri", "Sergio", "Fabienne"]
roles = create_roles_list(n_roles)

check_error_settings(names, roles)

random.shuffle(names)
