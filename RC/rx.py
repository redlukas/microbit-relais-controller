from microbit import *
import radio
radio.RATE_250KBIT
radio.on()

###initialise variables
counter = 0
i=0

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

def fadeinout(i):					###DO NOT USE WITH A RELAIS, ONLY MOSFET
    display.show("f")
    for i in range (250, 1023):
        pin2.write_analog(i)
        sleep(120)
    for i in range (1023, 250):
        pin2.write_analog(i)
        sleep(120)

###list containing the scenes, remember to add your scenes here
scenes = {0 : off, 1 : on, 2 : blink, 3 : fastblink, 4 : fadeinout}



while True:
	if counter >= len(scenes):				#reset the counter if all scenes have been played
        	counter = 0
	scenes[counter](i)
	now = counter						#so we know what we are playing
	while now == counter:			
		scenes[counter](i)			
		if button_a.was_pressed() == True:		#listen for the press of a button
			counter = counter + 1			#increment the counter on buttonpress
			break
		incoming = radio.receive()
        if incoming == "a":
			counter = counter + 1
			break