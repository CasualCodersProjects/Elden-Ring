import Play
from time import sleep
from multiprocessing import Process
import readkeypad

def play_sound(mp3_file):
    try:
        Play.play_music(mp3_file)
        sleep(.25)
    except Exception as e:
        print("error playing song")
        print(e)

if __name__ == '__main__':

    # find mp3 files on usb stick
      

    Play.init_sound()
    readkeypad.phone_setup()
    readkeypad.gpio_setup()

    while True:
        print('Program start! Welcome to the phone booth!')

        # Wait until handset is unplugged
        while(not readkeypad.check_phone_picked_up()):
            pass

        p = Process(target=play_sound, args=("~/../../mnt/usb/welcome.mp3"))
        p.start()

        # start looking at keypad
        while True:
            pressed_button = readkeypad.check_keypad_pressed()
            if pressed_button is not None:
                print(f'{pressed_button} was pressed!')
                p.kill()
                sleep(0.25)
                p = Process(target=play_sound, args=('~/../../mnt/usb/' + pressed_button+'.mp3'))
                p.start()
                sleep(1)
            if not readkeypad.check_phone_picked_up():
                p.kill()
                break





