
import RPi.GPIO as GPIO
from time import sleep
ringer_pins = [13] 


def ringer_setup():
    GPIO.setup(ringer_pins[0], GPIO.OUT, initial=GPIO.LOW)

def ring():
    for i in range(25):
        GPIO.output(ringer_pins[0], GPIO.HIGH)
        sleep(1/40)
        GPIO.output(ringer_pins[0], GPIO.LOW)
        sleep(1/40)


if __name__ == "__name__":
    ringer_setup()
    ring()