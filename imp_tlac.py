import RPi.GPIO as GPIO
import time

trigger = False

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(8, GPIO.OUT)

while (1):
	if GPIO.input(7) == 0:
		if trigger == False:
			GPIO.output(8, GPIO.HIGH)
			trigger = True
			time.sleep(0.5)
		else:
			GPIO.output(8, GPIO.LOW)
			trigger = False
			time.sleep(0.5)
		
	time.sleep(0.1)
GPIO.cleanup()
