from microbit import *
import radio

radio.RATE_250KBIT
radio.on()

while True:
    if button_a.was_pressed == True:
        display.scroll(str(button_a.get_presses()))
        radio.send("A")
        display.scroll("A")
        sleep(500)
        display.clear()
