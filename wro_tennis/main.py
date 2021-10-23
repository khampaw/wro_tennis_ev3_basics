#!/usr/bin/env python3

from time import sleep
from ev3dev2.button import Button
from ev3dev2.sound import Sound
import subprocess as sp
import sys


# this is demo code for communicating between balls.py and main.py
s = Sound()
b = Button()
# Start balls.py as subprocess
child = sp.Popen(['python', 'balls.py'], stdout=sp.PIPE, bufsize=1, universal_newlines=True)
# wait for balls.py init all its libs
while 1:
    p = child.stdout.readline()
    if p[0:len(p) - 1] == "ready":
        s.beep()
        break
    else:
        # Due known bug sleep() is a must for Ev3-dev code in loops unless u want 100% of your cpu be taken by this loop
        sleep(0.01)
# now wait for start button to be pressed
while Button.ENTER not in b.buttons_pressed():
    sleep(0.01)
s.beep()
# loop over and print coordinates of detected balls on Display
i = 0
while 1:
    # request for balls detected
    child.communicate(i)
    s = child.stdout.readline()
    # Your code goes here
    if s [0:len(s) - 1] == "NONE":
        # if none balls found branch
        print(s)
    else:
        # if balls found branch
        print(s)
        
    sleep(0.01)
