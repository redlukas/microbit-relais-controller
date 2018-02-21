from microbit import *

counter = 0

scnCount = 3



def off():
	pin2.write_digital(0)
	display.scroll("off")
	counter = button_a.get_presses + counter
	
def on():
	pin2.write_digital(1)
	display.scroll("on")
	counter = button_a.get_presses + counter

def blink():
	pin2.write_digital(1)
	sleep(500)
	pin2.write_digital(0)
	sleep(500)
	display.scroll("blink")
	counter = button_a.get_presses + counter
	
while true:
	if counter % scnCount == 0:
	off()
	
	elif counter % scnCount == 1:
		on()

	elif counter % scnCount == 2:
		blink()

	else:
		display.scroll("ka")
