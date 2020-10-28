from gpiozero import PWMLED, MCP3008
from time import sleep

yinput = MCP3008(0)
xinput = MCP3008(1)
yled = PWMLED(17)
xled = PWMLED(27)

while True:

	print("yposition: ", yinput.value, "	xposition", xinput.value)
	yled.value = yinput.value
	xled.value = xinput.value
	sleep(0.5)
