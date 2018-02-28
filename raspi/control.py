import RPi.GPIO as GPIO
import time

counter = 0

###set the GPIO in/output pin
outPin=17
inPin=27

###set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(outPin,GPIO.OUT)
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


###functions for the different scenes
def off():
	GPIO.output(outPin,GPIO.LOW)
	print "0" + "\r",

def on():
	GPIO.output(outPin,GPIO.HIGH)
	print "1" + "\r",

def blink():
	print "b" + "\r",
	GPIO.output(outPin,GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(outPin,GPIO.HIGH)
	time.sleep(0.5)

def fastblink():
	print "B" + "\r",
	GPIO.output(outPin,GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(outPin,GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(outPin,GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(outPin,GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(outPin,GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(outPin,GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(outPin,GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(outPin,GPIO.HIGH)
	time.sleep(0.1)

###list containing the scenes, remember to add your scenes here
scenes = {0 : off, 1 : on, 2 : blink, 3 : fastblink}



while True:
	if counter >= len(scenes):
        	counter = 0
	scenes[counter]()
	now = counter
	while now == counter:
		scenes[counter]()
		print "waiting" + "\r",
		input_state = GPIO.input(inPin)
		if input_state == True:
			counter = counter + 1
			time.sleep(1)
			print " "
			break

   
