import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(8, GPIO.OUT)

while (1):
	if GPIO.input(7) == 0:
		GPIO.output(8, GPIO.HIGH)
		time.sleep(3)
		GPIO.output(8, GPIO.LOW)
	time.sleep(0.5)
GPIO.cleanup()
