
import sys
import time
import datetime

import Adafruit_DHT

FREQUENCY_SECONDS = 30
SENSOR = Adafruit_DHT.AM2302
PIN = 4

file = open('dht.log', 'a+')

while True:
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    if humidity is not None and temperature is not None:
        output = '{}, {}, {}\n'.format(datetime.datetime.now().timestamp(), temperature, humidity)
    else:
        output = '{}, Failed to get reading'.format(datetime.datetime.now().timestamp())
    print(output)
    file.write(output)
    time.sleep(FREQUENCY_SECONDS)
