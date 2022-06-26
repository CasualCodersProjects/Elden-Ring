import RPi.GPIO as GPIO
from time import sleep
import signal
import sys


def signal_handler(sig, frame):
    print('You pressed Ctrl+C, cleaning up gpio...')
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

phone_pins = [5,6,12,13]
keypad_pins = [4,17,27,22,23,24,25]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


def readKeypad(printVal, inputPin, outputPin):
    #cleanup
    gpio_setup()

    # set output pin
    GPIO.setup(inputPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # set other input pin
    GPIO.setup(outputPin, GPIO.OUT, initial=GPIO.LOW)
    # if input is low its pressed
    if not GPIO.input(inputPin):
        return(printVal)
    else:
        return(None)

def gpio_setup():
    for pin in keypad_pins:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)

def update_result(result_so_far, param):
    if param is None:
        return result_so_far
    else:
        return param

# passes None if nothing is pressed, otherwise a string containing what was pressed
# (if more than 1 is pressed it only 1 is returned)
def check_keypad_pressed():
    result = None
    result = update_result(result,readKeypad("#", keypad_pins[3], keypad_pins[6]))
    result = update_result(result,readKeypad("6", keypad_pins[3], keypad_pins[1]))
    result = update_result(result,readKeypad("9", keypad_pins[3], keypad_pins[0]))
    result = update_result(result,readKeypad("0", keypad_pins[4], keypad_pins[6]))
    result = update_result(result,readKeypad("star", keypad_pins[5], keypad_pins[6]))
    result = update_result(result,readKeypad("7", keypad_pins[5], keypad_pins[0]))
    result = update_result(result,readKeypad("4", keypad_pins[5], keypad_pins[1]))
    result = update_result(result,readKeypad("1", keypad_pins[5], keypad_pins[2]))
    result = update_result(result,readKeypad("2", keypad_pins[4], keypad_pins[2]))
    result = update_result(result,readKeypad("3", keypad_pins[2], keypad_pins[3]))
    result = update_result(result,readKeypad("5", keypad_pins[1], keypad_pins[4]))
    result = update_result(result,readKeypad("8", keypad_pins[0], keypad_pins[4]))

    return result

def phone_setup():
    for pin in phone_pins:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# returns true if phone is picked up
def check_phone_picked_up():
    print(f'phone pins are {GPIO.input(phone_pins[0])} and {GPIO.input(phone_pins[3])}')
    return GPIO.input(phone_pins[0]) or GPIO.input(phone_pins[3])
