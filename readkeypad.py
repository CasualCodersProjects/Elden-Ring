import RPi.GPIO as GPIO
from time import sleep
import signal
import sys

GPIO.setwarnings(False)

def signal_handler(sig, frame):
    print('You pressed Ctrl+C')
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

used_pins = [7,8,10,11,12,13,15]

def readKeypad(printVal, inputPin, outputPin):
    print(f'powering pin {outputPin}')
    print(f'reading pin {inputPin}')
    # set_all_pins_input()
    # set output pin
    GPIO.setup(inputPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    # set other input pin
    GPIO.setup(outputPin, GPIO.OUT, initial=GPIO.HIGH)
    # if input is low its pressed

    # print_all_pins()    

    if not GPIO.input(inputPin):
        print(printVal)

    #cleanup
    setup()

# everything starts low
def setup():
    for pin in used_pins:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        

def set_all_pins_input():
    for i in range(0,6):
        GPIO.setup(used_pins[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)

def print_all_pins():
    for i in range(0,6):
        print(f'Pin {used_pins[i]} is a {GPIO.input(used_pins[i])}')
    sleep(4)


if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    setup()

    print("starting keypad detection...")

    while True:
        readKeypad("#", used_pins[3], used_pins[6])
        # readKeypad("6", used_pins[3], used_pins[1])
        # readKeypad("9", used_pins[3], used_pins[0])
        # readKeypad("0", used_pins[4], used_pins[6])
        # readKeypad("*", used_pins[5], used_pins[6])
        # readKeypad("7", used_pins[5], used_pins[0])
        # readKeypad("4", used_pins[5], used_pins[1])
        # readKeypad("1", used_pins[5], used_pins[2])
        # readKeypad("2", used_pins[4], used_pins[2])
        # readKeypad("3", used_pins[2], used_pins[3])
        # readKeypad("5", used_pins[1], used_pins[4])
        # readKeypad("8", used_pins[0], used_pins[4])
