"""Connect the moisture sensor to relay to solenoid"""


from chirp import Chirp

from gpiozero import LED
import time

led = LED(17)
"from chirp import Chirp"

addr = 0x20
min_moist = 240
max_moist = 750

highest_measurement = False
lowest_measurement = False

    # Initialize the sensor.
chirp = Chirp(address=addr,
                read_moist=True,
                read_temp=True,
                read_light=True,
                min_moist=min_moist,
                max_moist=max_moist,
                temp_scale='celsius',
                temp_offset=0)



# These values needs to be calibrated for the percentage to work!
# The highest and lowest value the individual sensor outputs.


try:
    print('Moisture  | Temp   | Brightness')
    print('-' * 31)
    while True:
        # Trigger the sensors and take measurements.
        chirp.trigger()
        output = '{:d} {:4.1f}% | {:3.1f}°C | {:d}'
        output = output.format(chirp.moist, chirp.moist_percent,
                               chirp.temp, chirp.light)
        
        ##REMOVE THE BOTTOM SINCE IT JUST TURNS ON LED WHEN MOISTURE IS BELOW 300
        if(chirp.moist<300):
            print("Hello mr. donkey")
            led.on()
            time.sleep(5)
            led.off()
        print(output)
        time.sleep(1)
except KeyboardInterrupt:
    print('\nCtrl-C Pressed! Exiting.\n')
finally:
    print('Bye! You are very rude!!')
    

#sensor.trigger()
#moisture = sensor.moist
#print(sensor.moist)

#if moisture < 300:
#    
