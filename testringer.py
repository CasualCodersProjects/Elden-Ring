from fastapi import FastAPI
import readkeypad
import RPi.GPIO as GPIO
from multiprocessing import Process
import multiprocessing
from time import sleep

ring_process = None

if __name__ == '__main__':
    freeze_support()


ringer_pins = [13]
ring_queue = multiprocessing.Queue()


app = FastAPI()

@app.on_event('startup')
def init_data():
    ring_process = Process(target=ringer_process_target,args=(ring_queue,))
    ring_process.start()
    readkeypad.phone_setup()
    return

@app.get("/start")
def start_ring():
    ring_queue.put(True)
    return {"ring": "started"}

@app.get("/stop")
def stop_ring():
    ring_queue.put(False)
    return {"ring": "stopped"}

@app.get("/ring25")
def ring_25():
    ring()
    return {"ringing": "25"}

def ringer_process_target(queue):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ringer_pins[0],GPIO.OUT, initial=GPIO.HIGH)
    readkeypad.phone_setup()
    should_ring = False
    while True:
        if not queue.empty():
            should_ring = queue.get()
        if should_ring:
            if readkeypad.check_phone_hung_up():
                # only ring phone if it is hung up
                GPIO.output(ringer_pins[0], GPIO.LOW)
                sleep(1/40)
                GPIO.output(ringer_pins[0], GPIO.HIGH)
                sleep(1/40)

def ringer_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ringer_pins[0], GPIO.OUT, initial=GPIO.HIGH)

def ring():
    for i in range(25):
        GPIO.output(ringer_pins[0], GPIO.LOW)
        sleep(1/40)
        GPIO.output(ringer_pins[0], GPIO.HIGH)
        sleep(1/40)

ringer_setup()

