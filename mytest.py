from gpiozero import PWMLED, MCP3008
from time import sleep

input = MCP3008(0)
led = PWMLED(17)

while True:
	if(input.value < 0.04)
		led.value = 0
	
	else:
		led.value = pot.value

	print(pot.value)
	sleep(0.1)
