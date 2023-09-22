import RPi.GPIO as GPIO
from itertools import product
import random
import time


BUTTON_PIN = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)



def perms():
    options = [1, 0] # the states the switch can have, high or low
    n = 3 # the number of switches in the game
    perms_l = list(product(*(options,)*n))

    print(perms_l)
    print(len(perms_l))
    rand = random.randint(0, len(perms_l))
    print(perms_l[rand])
    return list(perms_l[rand])



def buttons():
    try:
        while True:
            time.sleep(0.1)
            if GPIO.input(BUTTON_PIN) == GPIO.LOW:
                print("Button is pressed")
            else:
                print("Nothing can be see...")
    except KeyboardInterrupt:
        GPIO.cleanup



def main():
    Lperms = perms()
    print(perms)

    

if __name__ == "__main__":
    perms()
