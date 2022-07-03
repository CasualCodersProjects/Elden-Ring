from concurrent.futures import process
import multiprocessing
import Play
from time import sleep
from multiprocessing import Process
import readkeypad
import os

class soundplayer:

    def __init__(self,play_outro,repeat):
        self.using_backup = False
        self.repeat = repeat
        self.play_outro = play_outro
        self.sound_queue = multiprocessing.Queue()
        self.sound_process = Process(target=play_sound_with_queue, args=(self.sound_queue,self.play_outro,self.repeat,))
        self.sound_process.start()
        self.backup_sound_queue = multiprocessing.Queue()
        self.backup_sound_process = Process(target=play_sound_with_queue, args=(self.backup_sound_queue,self.play_outro,self.repeat,))
        self.backup_sound_process.start()
        
    def start_playing(self, mp3_file):
        print('starting play')
        if not self.using_backup:
            self.sound_queue.put(mp3_file)
        else:
            self.backup_sound_queue.put(mp3_file)

    def stop_playing(self):
        print('stopping play')

        if not self.using_backup:
            self.sound_process.kill()
            while not self.sound_queue.empty():
                self.sound_queue.get()
            self.sound_process = Process(target=play_sound_with_queue, args=(self.sound_queue,self.play_outro,self.repeat,))
            self.sound_process.start()
            self.using_backup = True
            print('now using backup process')
        else:
            self.backup_sound_process.kill()
            while not self.backup_sound_queue.empty():
                self.backup_sound_queue.get()
            self.backup_sound_process = Process(target=play_sound_with_queue, args=(self.backup_sound_queue,self.play_outro,self.repeat,))
            self.backup_sound_process.start()
            self.using_backup = False




def play_sound_with_queue(queue,play_outro,repeat):
    Play.init_sound()

    # wait for queue to play
    print('sound init, waiting to play')
    mp3_file = queue.get()
    print('recieved item! now will play!')

    if os.path.exists(mp3_file):
        try:
            if not repeat:
                Play.play_music(mp3_file)
            else:
                while True:
                    Play.play_music(mp3_file)
            sleep(.25)
            if play_outro:
                Play.play_music('/mnt/usb/outro.mp3')
        except Exception as e:
            print("error playing song")
            print(e)
    else:
        print(f'no mp3 found for {mp3_file}')


if __name__ == '__main__':
    # find mp3 files on usb stick
      
    readkeypad.phone_setup()
    readkeypad.gpio_setup()

    intro_soundplayer = soundplayer(play_outro=False,repeat=True)
    song_soundplayer = soundplayer(play_outro=True,repeat=False)
    print('Program start! Welcome to the phone booth!')
    
    while True:
        print('Device hung up. Waiting for pickup...')

        # Wait until handset is unplugged
        while(readkeypad.check_phone_hung_up()):
            pass
        print('Phone was picked Up!')

        intro_soundplayer.start_playing('/mnt/usb/welcome.mp3')

        intro_has_been_stopped = False
        song_has_started_playing = False
        # start looking at keypad
        while True:
            pressed_button = readkeypad.check_keypad_pressed()
            if pressed_button is not None:
                print(f'{pressed_button} was pressed!')
                if not intro_has_been_stopped:
                    intro_soundplayer.stop_playing()
                    intro_has_been_stopped = True
                song_soundplayer.start_playing(f'/mnt/usb/{pressed_button}.mp3')
                song_has_started_playing = True
                break
            if readkeypad.check_phone_hung_up():
                if not intro_has_been_stopped:
                    intro_soundplayer.stop_playing()
                    intro_has_been_stopped = True
                break
        # Do nothing until someone hangs up the phone
        while not readkeypad.check_phone_hung_up():
            pass
        if song_has_started_playing:
            song_soundplayer.stop_playing()

