import Play
from time import sleep
from multiprocessing import Process
import readkeypad

def play_sound(mp3_file):
    Play.init_sound()
    try:
        Play.play_music(mp3_file)
        sleep(.25)
    except Exception as e:
        print("error playing song")
        print(e)

if __name__ == '__main__':

    # find mp3 files on usb stick
      
    readkeypad.phone_setup()
    readkeypad.gpio_setup()

    while True:
        print('Program start! Welcome to the phone booth!')

        # Wait until handset is unplugged
        while(readkeypad.check_phone_picked_up()):
            pass
        print('Phone was picked Up!')

        p = Process(target=play_sound, args=('~/../../mnt/usb/welcome.mp3',))
        p.start()

        # start looking at keypad
        while True:
            pressed_button = readkeypad.check_keypad_pressed()
            if pressed_button is not None:
                print(f'{pressed_button} was pressed!')
                p.kill()
                sleep(0.25)
                p = Process(target=play_sound, args=('~/../../mnt/usb/' + pressed_button+'.mp3',))
                p.start()
                sleep(1)
            if readkeypad.check_phone_picked_up():
                p.kill()
                break





