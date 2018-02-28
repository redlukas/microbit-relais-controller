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
	print "0"

def on():
	GPIO.output(outPin,GPIO.HIGH)
	print "1"

def blink():
	print "B"
	GPIO.output(outPin,GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(outPin,GPIO.LOW)
	time.sleep(0.5)

###list containing the scenes, remember to add your scenes here
scenes = {0 : off, 1 : on, 2 : blink}

while True:
	if counter > 2:
        	counter = 0
	scenes[counter]()
	now = counter
	while now == counter:
		input_state = GPIO.input(inPin)
		if input_state == True:
			counter = counter + 1
			time.sleep(1)
			print "waiting"
			time.sleep(2)
		else:
			break

   