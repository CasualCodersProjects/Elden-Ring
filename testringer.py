from fastapi import FastAPI

import RPi.GPIO as GPIO
from time import sleep
ringer_pins = [13] 


app = FastAPI()

@app.get("/")
def read_root():
    ring()
    return {"Hello": "World"}

def ringer_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ringer_pins[0], GPIO.OUT, initial=GPIO.LOW)

def ring():
    for i in range(25):
        GPIO.output(ringer_pins[0], GPIO.HIGH)
        sleep(1/40)
        GPIO.output(ringer_pins[0], GPIO.LOW)
        sleep(1/40)

ringer_setup()


if __name__ == "__main__":
    
    ring()