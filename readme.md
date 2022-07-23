# Project Eldin Ring

Eldin ring is a project where an old phone from a phone booth is being trasformed into a device that can play audio.


# setup

This project is using a 
- raspberry pi zero [pinout](https://pinout.xyz)
- adafruit i2s audio bonnet: [docs](https://learn.adafruit.com/adafruit-i2s-audio-bonnet-for-raspberry-pi/pinouts)
- keypad (from the phone)
- speakers x 2

All pinout uses the BCM layout

adafruit i2s audio bonnet
used pins:
18
19
21
16
20

ringer_pins = [13] 
phone_pins = [5,6]
keypad_pins = [4,17,27,22,23,24,25]



# Usage

### phone setup
First, plug in the phone booth. After about 1 min 30 seconds the bell should ring signifying that it is up and running.

### Web usage
The phone booth emits wifi called `Phone Booth`. Once connected, open a browser and connect to http://192.168.4.1 in the url search bar. You will see a website with a bell icon.

When you hold down the bell icon, it rings the bell. When you let go it stops the bell. If you close the browser without letting go on the bell it will continue to ring until you open the app and click the bell again or pick up the phone.

The bell only rings when the phone is hung up.

### Adding Music to the phone
Power off the device. Take out the usb drive and replace the mp3 files on it.
Plug in the usb drive and power on the phone booth.
If the phone booth does not have a usb drive when it is turned on it will not boot.
power off the device, re-plug in the usb drive, and the phone booth should turn on in 1 min, 30 seconds(ish).

### Phone Behavior

The phone is silent until the handset is picked up. When handset is picked up it plays welcome.mp3

if a key is pressed, welcome.mp3 is stopped and it starts playing the audio associated with the pressed key. once the song is over, the payphone will be silent.

any time the payphone is hung up it goes silent.


# Installation of a new payphone

install autoservice for mounting usb/sda1 to /mnt/usb
install autoservice for the adafruit pihat to stop audio crackle

```
python -m venv ./venv
source venv/bin/activate
pip install -r requirements.txt
```

add to cron the path to the autostart scripts

