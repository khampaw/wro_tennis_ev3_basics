import cv2
import cv2.cv as cv
import numpy as np
from time import sleep

"""
Made by Pavel Khamenya 
If you got any questions please contact me via:
khamparobotics@gmail.com
"""

# Let main process know that this subprocess loaded all reqired libraries and started working
print('ready')
# Initialize the requred camera
cap = cv2.VideoCapture(0)

# Set width and height of frames 
cap.set(3,160)
cap.set(4,120)


while(1):
	# read fresh frame
	_, frame = cap.read()
	# wait for new idx
	# use resize if your camera does not support set
	frame = cv2.resize(frame, (160, 120))
	# Use flip if your image are mirrored
	frame = cv2.flip(frame, 1)
	# make frame hsv for future operations
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	hue,sat,val = cv2.split(hsv)
	# set minimal and maximal hue
	hmn = 5
	hmx = 25
	# set minmial and maximal saturation
	smn = 50
	smx = 255
	# set minimal and maximal value
	vmn = 50
	vmx = 255
	# You may see support_hsv.png for more help
	# thresholding goes brrr...
	hthresh = cv2.inRange(np.array(hue),np.array(hmn),np.array(hmx))
	sthresh = cv2.inRange(np.array(sat),np.array(smn),np.array(smx))
	vthresh = cv2.inRange(np.array(val),np.array(vmn),np.array(vmx))
	# connect thresholding h, s, v
	tracking = cv2.bitwise_and(hthresh,cv2.bitwise_and(sthresh,vthresh))
		
	# Erode/Dilate 
	# erode = cv2.erode(tracking,None, iterations = 2)
	# dilation = cv2.dilate(erode,None, iterations = 2)
	
	# Advanced alternative of erode/dilate
	closing = cv2.morphologyEx(tracking, cv2.MORPH_CLOSE, None, iterations = 2)

	# ...and we blur it after
	closing = cv2.GaussianBlur(closing,(11,11),0)

	# Locate circles, read docs about parameters before shaping it up
	circles = cv2.HoughCircles(closing,cv.CV_HOUGH_GRADIENT,2, 60,param1=120,param2=30,minRadius=1,maxRadius=0)
	# OpenCV v3+ 
	#circles = cv2.HoughCircles(closing, cv2.HOUGH_GRADIENT,2,60,param1=120,param2=30,minRadius=1,maxRadius=0)
		
	# Guess the largest circle
	if circles is not None:
		# c[0] is x, c[1] is y, and c[2] is radius of cirlce
		c = max(circles[0,:], key=lambda item:item[2])
		print(str(c[0]) + " " + str(c[1]) + " " + str(c[2]))
	else:
		print('NONE')
	
	# Due known bug sleep() is a must for Ev3-dev programs in loops unless u want 100% of your cpu be taken by this loop
	sleep(0.01)

cap.release()
