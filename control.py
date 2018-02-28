from microbit import *

counter = button_a.get_presses
scnCount = 3

def off():
	global counter
	pin2.write_digital(0)
	display.scroll("0")
	counter = counter + button_a.get_presses

def on():
	global counter
	pin2.write_digital(1)
	display.scroll("1")
	counter = counter + button_a.get_presses

def blink():
	global counter
	pin2.write_digital(1)
	sleep(500)
	pin2.write_digital(0)
	sleep(500)
	display.scroll("B")
	counter = counter + button_a.get_presses

while counter == 0:
	off()

while counter == 1:
	on()

while counter == 2:
	blink()

if counter > 2:
	counter = 0
