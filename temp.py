from itertools import product
import random
import time


def code_gen():
    options = [1, 0] # the states the switch can have, high or low
    n = 3 # the number of switches in the game

    perms_list = list(product(*(options,)*n))

    last_item = len(perms_list) - 1

    perms_list.pop(last_item)
    print(perms_list)
    
    rand = random.randint(0, len(perms_list) - 1)
    return list(perms_list[rand])


def code_gen2():
    options = [1, 0] # the states the switch can have, high or low
    n = 3 # the number of switches in the game

    perms_list = list(product(*(options,)*n))

    print(perms_list)
    
    rand = random.randint(0, len(perms_list) - 1)
    return list(perms_list[rand])



def main():
    code_gen()



if __name__ == "__main__":
    main()
