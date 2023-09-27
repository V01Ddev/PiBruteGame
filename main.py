import RPi.GPIO as GPIO
from itertools import product
import random
import time


"""
GUI: * Use Guizero to make a pop up for when the code is broken
    * Start again button to reset
"""



SWITCH_1 = 22
SWITCH_2 = 27
SWITCH_3 = 17

GREEN_LED = 24
RED_LED = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(SWITCH_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SWITCH_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SWITCH_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)


GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

# TO SET STATUS
# GPIO.output(GREEN_LED, GPIO.HIGH)

def code_gen():
    options = [1, 0] # the states the switch can have, high or low
    n = 3 # the number of switches in the game

    perms_list = list(product(*(options,)*n))

    last_item = len(perms_list) - 1

    perms_list.pop(last_item)
    
    rand = random.randint(0, len(perms_list) - 1)

    return list(perms_list[rand])



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



def flashing(pin):

    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)

    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)

    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)

    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)

    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)




def game():

    code = code_gen()
    print(code) # REMOVE IN PRODUCTION

    GPIO.output(RED_LED, GPIO.HIGH)

    for i in range(3, 0, -1):
        time.sleep(1)
        print(f"Game starting in {i}...")

    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(GREEN_LED, GPIO.HIGH)

    start_time = time.time()

    game_won = False

    while game_won == False:
        if ButtonStats() == code:
            game_won = True

            print(f"CODE BROKEN! {code}")
            time_taken = round(time.time() - start_time, 2)
            print(time_taken)

            print("Flashing LED")

            flashing(GREEN_LED)

    GPIO.output(RED_LED, GPIO.HIGH)




def main():
    game()

    try:
        while True:
            res = str(input("Press enter to restart (ctrl-C to quit) "))
            game()

    except KeyboardInterrupt:
        GPIO.cleanup



if __name__ == "__main__":
    main()
