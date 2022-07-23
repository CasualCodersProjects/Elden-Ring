# Project Elden Ring
Designed in Part by Casual Coders

## Setup and Unboxing
Upon reception of the project, use the key to carefully remove the top cover of the phone. Be careful and avoid snagging or pulling on wires. You'll need to connect the red MicroUSB cable to the top microUSB port of the raspberry pi.  

You'll also need to connect the 20v supply for the bell. The supply is labled with it's connections, and there are screw terminals which are also labeled.

## User Documentation
The way a user is expected to interact with Elden Ring is through the handset and the keypad. When power is applied to the raspberry Pi through it’s top USB Port, it will boot up (Only if the USB Stick is installed) and be ready to interface with (Boot times may be as long as five minutes). When the handset is lifted from the hook, welcome.mp3 will repeatedly play until a selection of the 12 keys is pressed. An audio file, named according to the key, will be played and an ending message will follow. The audio files for the keypads are 0-9.mp3, star.mp3, and #.mp3. The ending message is called outro.mp3. All of these files live in the root of the included USB Drive, which is located in the coinbox of the phone. 

To ring the bell, connect to the Booth wireless network (Password of EldenRing) and navigate to 192.168.4.1 in an internet browser. You should be greeted with a page that looks like this:
![Webpage](/images/Webpage.png)
Clicking the bell icon will cause the bell to ring in some way as defined by the client.  
Additionally, you can connect to the Booth wireless network and SSH into the raspberry pi (192.168.4.1) at the heart of the project. The raspberry pi has a username of `pi` and a password of `raspberry`. This is the default user for a raspberry pi.

## Hardware Documentation
### Wiring
#### Keypad
The keypad is a relatively simple part. We took it apart, reverse engineered the switch matrix, and connected it straight to the GPIOs of the raspberry pi. The following image shows the disassembled keypad with the raspberry pi GPIO pin Numbers (The BCM numbers, [GPIO XX]) overlaid.  
![Keypad](/images/Keypad%20Wiring.png)
The keypad has an 8-pin Dupont (2.54mm pitch) connector which attaches to the 8-pin header. The side labeled “away” should face away from the audio ports as shown in the following image.
![Keypad Connection](/images/keypad%20connection.jpg)
#### Hook
The hook is even more basic, just being a set of 2 switches. This breaks out into a 2 pin Dupont (2.54mm pitch) connector which attaches to the 4-pin header, closest to the 8-pin header as shown in the above photo. This connector is not polarized and can be connected either way.
#### Bell
The bell is the most complicated part, requiring a square wave of 96v at 20Hz. This is achieved by a DC_DC Boost converter running through a 3v3 relay module. The relay is powered off the 3v3 of the raspberry pi on the 2x3 pin power section of the audio hat. The relay then splits the high (positive) side of the 96v, configured for normally open operation (The relay acts as an open circuit, allowing no current to flow, when there is no power provided on the central in1 pin.)  

The in1 pin (white wire) connects to the far side of the 4-pin header as shown in the following photo.
![Bell Connection](/images/bell%20connection.jpg)

## Schematic
![Schematic](/images/Proj_EldenRing_Schematic.pdf)