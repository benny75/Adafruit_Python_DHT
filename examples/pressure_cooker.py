import time
import datetime
import Adafruit_DHT
from gpiozero import Energenie


PORT = 2
OFF_INTERVAL = 3.5
ON_INTERVAL = 1.25


def power_on():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Turning on cooker at {}".format(now))
    Energenie(PORT, initial_value=True)


def power_off():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Turning off cooker at {}".format(now))
    Energenie(PORT, initial_value=False)


#power_on()
#time.sleep(16 * 60)
while True:
    power_off()
    time.sleep(OFF_INTERVAL * 60)
    OFF_INTERVAL = OFF_INTERVAL + .05
    power_on()
    time.sleep(ON_INTERVAL * 60)
