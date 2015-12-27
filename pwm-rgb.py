import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

green = GPIO.PWM(8, 50)
red = GPIO.PWM(7, 50)
blue = GPIO.PWM(11, 50)

def rgb (r, g, b):
	red.start(0)
	green.start(0)
	blue.start(0)
	
	red.ChangeDutyCycle(r)
	green.ChangeDutyCycle(g)
	blue.ChangeDutyCycle(b)
	

rgb(100,0,0)
time.sleep(1)
rgb(0,100,0)
time.sleep(1)
rgb(0,0,100)
time.sleep(1)
rgb(100,100,0)
time.sleep(1)
rgb(100,0,100)
time.sleep(1)
rgb(0,100,100)
time.sleep(1)
rgb(100,100,100)
time.sleep(1)

red.stop()
blue.stop()
green.stop()
GPIO.cleanup()
