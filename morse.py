import RPi.GPIO as GPIO
import time

file = open("morse.txt", "r")
data = file.read()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

for letter in data:
	if letter == '.':
		GPIO.output(8, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(8, GPIO.LOW)
	if letter == '-':
		GPIO.output(8, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(8, GPIO.LOW)
 	if letter == ' ':
		time.sleep(0.5)
	if letter == '/':
		time.sleep(0.5)
	time.sleep(0.2)
	
