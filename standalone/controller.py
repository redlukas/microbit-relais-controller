from microbit import *

counter = 0

###set the GPIO in/output pin
outPin=2


###functions for the different scenes
def off():
	pin2.write_digital(0)
	display.show("0")

def on():
	pin2.write_digital(1)
	display.show("1")

def blink():
	display.show("b")
	pin2.write_digital(0)
	sleep(500)
	pin2.write_digital(1)
	sleep(500)

def fastblink():
	display.show("B")
	pin2.write_digital(0)
	sleep(500)
	pin2.write_digital(1)
	sleep(1000)

###list containing the scenes, remember to add your scenes here
scenes = {0 : off, 1 : on, 2 : blink, 3 : fastblink}



while True:
	if counter >= len(scenes):				#reset the counter if all scenes have been played
        	counter = 0
	scenes[counter]()					#rocknroll
	now = counter						#so we know what we are playing
	while now == counter:			
		scenes[counter]()			
		if button_a.was_pressed() == True:		#listen for the press of a button
			counter = counter + 1			#increment the counter on buttonpress
			break