import RPi.GPIO as GPIO
import time

used_pins = [3,5,7,8,10,11,12]
GPIO.setmode(GPIO.BOARD)

def readKeypad(whattoprint, input_pin, output_pin):
    GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.LOW)

readKeypad("#", used_pins[3], used_pins[6])
while True:
    print(used_pins[3])
    time.sleep(1)


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