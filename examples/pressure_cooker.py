import time
import datetime
import Adafruit_DHT
from gpiozero import Energenie


PORT = 2
OFF_INTERVAL = 3.2
ON_INTERVAL = 1
counter = 0


def power_on():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Turning on cooker at {}".format(now))
    Energenie(PORT, initial_value=True)


def power_off():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Turning off cooker at {}".format(now))
    Energenie(PORT, initial_value=False)


while True:
    counter = counter + 1
    power_off()
    time.sleep(OFF_INTERVAL * 60)
    OFF_INTERVAL = OFF_INTERVAL + .1
    power_on()
    if counter <= 3:
        time.sleep((ON_INTERVAL+0.3) * 60)
    else:
        time.sleep(ON_INTERVAL * 60)
