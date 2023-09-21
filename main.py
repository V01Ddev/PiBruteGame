import RPi.GPIO as GPIO
from itertools import permutations
import random
import time


BUTTON_PIN = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)



def perms():
    perms_list = list(permutations(range(1, 4)))
    rand = random.randint(0, 5)
    print(perms_list[rand])
    return list(perms_list[rand])



def buttons:
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
