import RPi.GPIO as GPIO
from guizero import App, Text, PushButton
from itertools import product
import random
import time


"""
Time:
    * take time when function first starts running using time module find time after code is broken then get the delta and display it.
GUI:
    * Use Guizero to make a pop up for when the code is broken
    * Start again button to reset

"""



SWITCH_1 = 17
SWITCH_2 = 27
SWITCH_3 = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(SWITCH_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SWITCH_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SWITCH_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)



def code_gen():
    options = [1, 0] # the states the switch can have, high or low
    n = 3 # the number of switches in the game

    perms_l = list(product(*(options,)*n))

    rand = random.randint(0, len(perms_l))
    return list(perms_l[rand])



def ButtonStats():

    sw = []

    if GPIO.input(SWITCH_1) == GPIO.LOW:
        sw.append(1)
    else:
        sw.append(0)
    
    if GPIO.input(SWITCH_2) == GPIO.LOW:
        sw.append(1)
    else:
        sw.append(0)

    if GPIO.input(SWITCH_3) == GPIO.LOW:
        sw.append(1)
    else:
        sw.append(0)
    
    return sw



def game():

    code = code_gen()
    
    for i in range(3):
        print("Game stating in {i}...")
        time.sleep(1)

    start_time = time.time()
    While game_state = True:
        if ButtonStats() == code:
            print(f"CODE {code} BROKEN!")
            print(time.time() - start_time)



def main():
    game()

    while True():
        res = str(input("Press enter to restart (ctrl-C to quit) "))
        game()

    except KeyboardInterrupt:
        GPIO.cleanup



if __name__ == "__main__":
    main() 
