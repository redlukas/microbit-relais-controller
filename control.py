from microbit import *

counter = 0

scnCount = 3

def incrementer():
	if button_a.is_pressed()
		counter = counter + 1

incrementer()


if counter % scnCount == 0:
	pin2.write_digital(0)
	display.scroll("off")
	
elif counter % scnCount == 1:
	pin2.write_digital(1)
	display.scroll("on")

elif counter % scnCount == 2:
	pin2.write_digital(1)
	sleep(500)
	pin2.write_digital(0)
	sleep(500)
	display.scroll("blink")

else:
	display.scroll("?")

