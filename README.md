# wro_tennis_ev3_basics
Basic project for wro tennis and Ev3 simple and allows you detect balls in subprocess

1. You required to install ev3-dev on your ev3 to use this solution HowTo: https://www.ev3dev.org/docs/getting-started/
2. You requried to install opencv v2.4.9.1 on your ev3
3. You reqired to install numpy on ev3


How does this work:
1. We got balls.py which detects circles of set color and returns (x, y, radius) of largest circle, and launched as subprocess from main.py it awaits for number in order to operate with fresh frames
2. We got main.py which first awaits for balls.py to load it's libraries(takes about ~30 seconds it's a big deal in term of competition) then it awaits you to press ENTER button to launch your main program(allowed by rules as you've got ~90 sec for robot to setup) 
3. To ask for a largest ball on frame:
4. Send a number via communicate() method which differs from previous number
5. if it is any circles of requred hsv balls.py will send (x, y, radius) of largest ball, else it will send "NONE" string
