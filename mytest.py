from gpiozero import PWMLED, MCP3008
from time import sleep

yinput = MCP3008(0)
xinput = MCP3008(1)
upled = PWMLED(4)
downled = PWMLED(14)
leftled = PWMLED(15)
rightled = PWMLED(18)

while True:

	print("yposition: ", yinput.value, "	xposition", xinput.value)

	#up/down movement

	if(yinput.value <0.51 and yinput.value >0.48): #taking care of when joystick is in the middle
		upled.value = 0
		downled.value = 0
 
	elif(yinput.value <0.5):
		upled.value = (0.5 - yinput.value)
		downled.value = 0
	else:
		downled.value = (yinput.value - 0.5)
		upled.value = 0

	#right/left movement

	if(xinput.value <0.51 and xinput.value >0.49): #when joystick is in the middle
		rightled.value = 0
		leftled.value = 0

	elif(xinput.value  <0.5):
		leftled.value = (0.5 - xinput.value)
		rightled.value = 0
	else:
		rightled.value = (xinput.value - 0.5)
 		leftled.value = 0
	
	sleep(0.05)
