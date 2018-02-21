from microbit import *

counter = button_a.get_presses
scnCount = 3

def off():
	pin2.write_digital(0)
	display.scroll("0")
	counter = counter + button_a.get_presses
	
def on():
	pin2.write_digital(1)
	display.scroll("1")
	counter = counter + button_a.get_presses

def blink():
	pin2.write_digital(1)
	sleep(500)
	pin2.write_digital(0)
	sleep(500)
	display.scroll("B")
	counter = counter + button_a.get_presses
	
while True:
	if counter == 0:
		off()
	
	elif counter == 1:
		on()

	elif counter == 2:
		blink()

	else:
		display.scroll("k")