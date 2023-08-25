from gpiozero import LED, Button
from time import sleep

green_led = LED(22)
yellow_led = LED(27)
red_led = LED(17)

while True:
    red_led.on()
    sleep(4)
    red_led.off()
    yellow_led.on()
    sleep(2)
    yellow_led.off()
    green_led.on()
    sleep(4)
    green_led.off()
    yellow_led.on()
    sleep(2)
    yellow_led.off()
    
