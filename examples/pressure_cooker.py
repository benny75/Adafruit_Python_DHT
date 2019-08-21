import time
import datetime
import Adafruit_DHT
from gpiozero import Energenie


PORT = 1


def power_on():
    Energenie(PORT, initial_value=True)


def power_off():
    Energenie(PORT, initial_value=False)


power_on()
time.sleep(17 * 60)
while True:
    power_off()
    time.sleep(3.5 * 60)
    power_on()
    time.sleep(1.5 * 60)
