import multiprocessing
import Play
from time import sleep
from multiprocessing import Process
import readkeypad
import os

def play_sound(mp3_file):
    Play.init_sound()

    # wait for queue to play

    if os.path.exists(mp3_file):
        try:
            Play.play_music(mp3_file)
            sleep(.25)
        except Exception as e:
            print("error playing song")
            print(e)
    else:
        print(f'no mp3 found for {mp3_file}')

def play_sound_with_queue(mp3_file,queue):
    Play.init_sound()

    # wait for queue to play
    print('sound init, waiting to play')
    obj = queue.get()
    sleep(1)
    print('recieved item! now will play!')

    if os.path.exists(mp3_file):
        try:
            Play.play_music(mp3_file)
            sleep(.25)
        except Exception as e:
            print("error playing song")
            print(e)
    else:
        print(f'no mp3 found for {mp3_file}')

def create_processes():
    
    queue = multiprocessing.Queue()

    processes = []

    p = Process(target=play_sound, args=('/mnt/usb/welcome.mp3',queue,))
    p.start()
    processes.append(p)
    for num in range(0,10):
        proc = Process(target=play_sound, args=(f'/mnt/usb/{num}.mp3',))
        proc.start()
        processes.append(proc)
    proc_hash = Process(target=play_sound, args=(f'/mnt/usb/#.mp3',))
    proc_hash.start()
    processes.append(proc_hash)
    proc_star = Process(target=play_sound, args=(f'/mnt/usb/star.mp3',))
    proc_star.start()
    processes.append(proc_star)


if __name__ == '__main__':
    # find mp3 files on usb stick
      
    readkeypad.phone_setup()
    readkeypad.gpio_setup()
    queue = multiprocessing.Queue()
    intro_process = Process(target=play_sound_with_queue, args=(f'/mnt/usb/welcome.mp3',queue))
 
    while True:
        intro_process.start()
        print('Program start! Welcome to the phone booth!')

        # Wait until handset is unplugged
        while(readkeypad.check_phone_picked_up()):
            pass
        print('Phone was picked Up!')

        queue.put("go")
        # p = Process(target=play_sound, args=('/mnt/usb/welcome.mp3',))
        # p.start()
        alive_processes = [intro_process]

        # start looking at keypad
        while True:
            pressed_button = readkeypad.check_keypad_pressed()
            if pressed_button is not None:
                print(f'{pressed_button} was pressed!')
                for process in alive_processes:
                    process.kill()
                intro_process = Process(target=play_sound_with_queue, args=(f'/mnt/usb/welcome.mp3',queue))
                intro_process.start() 
                alive_processes = []
                p = Process(target=play_sound, args=('/mnt/usb/' + pressed_button+'.mp3',))
                p.start()
                alive_processes.append[p]
                sleep(1)
            if readkeypad.check_phone_picked_up():
                for process in alive_processes:
                    process.kill()
                break

