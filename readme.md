# Project Eldin Ring

Eldin ring is a project where an old phone from a phone booth is being trasformed into a device that can play audio.


# setup

This project is using a 
- raspberry pi zero [pinout](https://pinout.xyz)
- adafruit i2s audio bonnet: [docs](https://learn.adafruit.com/adafruit-i2s-audio-bonnet-for-raspberry-pi/pinouts)
- keypad (from the phone)
- speakers x 2

adafruit i2s audio bonnet
used pins:
18
19
21
16
20

Keypad board pinout
Used pins (from right to left): 
13
15
7
8
10
11
12
ground



Usage

Mute always

when handset is picked up, play welcome.mp3

if a key is pressed, stop welcome.mp3 and start playing that audio
after any audio is stopped, it goes mute
(make someone hang up and pick up again?)

putting handset down stops audio playback


# Installation

install autoservice for mounting usb/sda1 to /mnt/usb
install autoservice for the adafruit pihat we are using

python -m venv ./venv
source venv/bin/activate
pip install -r requirements.txt
