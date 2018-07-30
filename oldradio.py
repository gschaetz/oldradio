#!/usr/bin/env python 
''' ********************************************************************** 
* Filename      : oldradio.py   
* Description - This app will control the old radio by turning on and 
* off the power for via relay control and will control the lights 
********************************************************************** ''' 
import RPi.GPIO as GPIO 
import time 
import pigpio

Relay_channel = 3
Left_led = 26 
Right_led = 16
Power_GPIO = 4
Power_state = 0

def setup():
	GPIO.setmode(GPIO.BCM)     
	GPIO.setup(Relay_channel, GPIO.OUT, initial=GPIO.HIGH)     
	GPIO.setup(Left_led, GPIO.OUT, initial=GPIO.LOW)     
	GPIO.setup(Right_led, GPIO.OUT, initial=GPIO.LOW)     
	
def main():     
	pi = pigpio.pi()
	if not pi.connected:
   		exit()


	# setup the gpio pin for PowerOnOff
	GPIO.setup(Power_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	# Add our function to execute when the button pressed event happens
	#GPIO.add_event_detect(Power_GPIO, GPIO.FALLING, callback = PowerOnOff, bouncetime = 2000)
	
	pi.set_glitch_filter(Power_GPIO, 100)
	pi.callback(Power_GPIO, pigpio.FALLING_EDGE, PowerOnOff)
	
	# wait for keyboard input to kill
	while True:
		time.sleep(1)

def PowerOnOff (gpio, level, tick):
	global Power_state

	print "poweronoff"
	if Power_state == 0:
		print '...Turning On'
		GPIO.output(Relay_channel, GPIO.LOW)
		GPIO.output(Left_led, GPIO.HIGH)
		GPIO.output(Right_led, GPIO.HIGH)
		Power_state = 1
	else:
		print '...Turning Off'
		GPIO.output(Relay_channel, GPIO.HIGH)
		GPIO.output(Left_led, GPIO.LOW)
		GPIO.output(Right_led, GPIO.LOW)
		Power_state = 0
 
def destroy():     
	GPIO.output(Relay_channel, GPIO.LOW)     
	GPIO.cleanup() 

if __name__ == '__main__':     
	setup()     
	
	try:         
		main()     
	except KeyboardInterrupt:         
		destroy()