import RPi.GPIO as GPIO
import time

dc = 10

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8, GPIO.OUT)
pwm = GPIO.PWM(8, 50)

pwm.start(dc)

for i in range(0,8):
	dc = dc + 10
	pwm.ChangeDutyCycle(dc)
	time.sleep(0.5)

for i in range(0,8):
	dc = dc - 10
	pwm.ChangeDutyCycle(dc)
	time.sleep(0.5)

pwm.stop()
GPIO.cleanup()

