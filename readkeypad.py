import RPi.GPIO as GPIO
from time import sleep
import signal
import sys

def signal_handler(sig, frame):
    print('You pressed Ctrl+C')
    GPIO.output(8, GPIO.cleanup())
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

used_pins = [3,5,7,8,10,11,12,13]

def readKeypad(printVal, inputPin, outputPin):
    # set output pin
    GPIO.setup(inputPin, GPIO.IN)
    # set other input pin
    GPIO.setup(outputPin, GPIO.OUT, initial=GPIO.HIGH)
    # if input is low its pressed
    if not GPIO.input(inputPin):
        print(printVal)

    #cleanup
    setup()

# everything starts low
def setup():
    for pin in used_pins:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)


if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    setup()

    print("starting keypad detection...")

    while True:
        readKeypad("#", used_pins[3], used_pins[6])
        readKeypad("6", used_pins[3], used_pins[1])
        readKeypad("9", used_pins[3], used_pins[0])
        readKeypad("0", used_pins[4], used_pins[6])
        readKeypad("*", used_pins[5], used_pins[6])
        readKeypad("7", used_pins[5], used_pins[0])
        readKeypad("4", used_pins[5], used_pins[1])
        readKeypad("1", used_pins[5], used_pins[2])
        readKeypad("2", used_pins[4], used_pins[2])
        readKeypad("3", used_pins[2], used_pins[3])
        readKeypad("5", used_pins[1], used_pins[4])
        readKeypad("8", used_pins[0], used_pins[4])
