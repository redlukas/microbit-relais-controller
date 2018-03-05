from microbit import *

###set up radio
def radioOn ():
    import radio
    radio.RATE_1MBIT
    radio.on()
    radio.config()
	
def radioOff ():
    radio.off()	

###initialise variables
counter = 0
radioState = 0

###set the GPIO in/output pin
outPin=2


###functions for the different scenes
def off(i):
	pin2.write_digital(0)
	display.show("0")

def on(i):
	pin2.write_digital(1)
	display.show("1")

def blink(i):
	display.show("b")
	pin2.write_digital(0)
	sleep(500)
	pin2.write_digital(1)
	sleep(500)

def fastblink(i):
	display.show("B")
	pin2.write_digital(0)
	sleep(900)
	pin2.write_digital(1)
	sleep(150)

def fadeinout(i):
    display.show("f")
    for i in range (0, 1023):
        pin2.write_analog(i)
    for i in range (1023, 0):
        pin2.write_analog(i)

###list containing the scenes, remember to add your scenes here
scenes = {0 : off, 1 : on, 2 : blink, 3 : fastblink, 4 : fadeinout}



while True:
	if counter >= len(scenes):				#reset the counter if all scenes have been played
        	counter = 0
	scenes[counter](i)					#rocknroll
	now = counter						#so we know what we are playing
	while now == counter:			
		scenes[counter](i)			
		if button_a.was_pressed() == True or radio.recieve() == "B":		#listen for the press of a button OR the Reception of a signal
			counter = counter + 1			#increment the counter on buttonpress
			break
		elif button_a.was_pressed() and button_b.was_pressed() == True:		#Toggle Radio states on A+B Press
		    radioState = radioState + 1
			if radioState % 2 == 0:
			    radioOff()
			elif radioState % 2 == 1:
			    radioOn()
		elif button_b.was_pressed() == True:					#send the signal to the other Microbit
		    radio.send("B")