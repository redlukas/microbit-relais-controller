import RPi.GPIO as GPIO
import time

###set the GPIO in/output pin
outPin=17
inPin=27

###set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(outPin,GPIO.OUT)
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)



while True:
    input_state = GPIO.input(inPin)
    if input_state == True:
        GPIO.output(outPin,GPIO.HIGH)
        #time.sleep(0.5)
    else:
        GPIO.output(outPin,GPIO.LOW)
