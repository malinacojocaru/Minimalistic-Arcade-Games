from machine import ADC, Pin
import time

adc_pins = [ADC(Pin(26)), ADC(Pin(27)), ADC(Pin(28))]

while True:
    readings = [adc.read_u16() for adc in adc_pins]
    print(readings)
    #Add sleep if needed
    #time.sleep(0.1)
