from microbit import *


import radio				###set up the radio module
radio.RATE_250KBIT
radio.on()


def sendit():				### the function to send the important command
	radio.send("a")

while True:
	if button_a.was_pressed() == True:
		sendit()
