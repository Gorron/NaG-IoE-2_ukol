import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.cleanup()

pins = [37, 33, 31, 29, 40, 38, 36, 32, 22, 18]

for i in pins:
	GPIO.setup(i, GPIO.OUT)

while 1:
	for i in pins:
		GPIO.output(i, GPIO.LOW)
		time.sleep(0.1)
		GPIO.output(i, GPIO.HIGH)
