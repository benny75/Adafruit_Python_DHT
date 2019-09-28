import time
import datetime
import Adafruit_DHT
from gpiozero import Energenie


PORT = 2


now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Turning off at {}".format(now))
Energenie(PORT, initial_value=False)
