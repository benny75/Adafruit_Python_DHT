
import time
import datetime
import Adafruit_DHT
from gpiozero import Energenie

FREQUENCY_SECONDS = 30
SENSOR = Adafruit_DHT.AM2302
PIN = 4

MIN_TEMP = 19
MAX_TEMP = 23
MIN_HUMID = 80
MAX_HUMID = 90

def write_to_file_and_sys():
    if humidity is not None and temperature is not None:
        output = '{}, {}, {}\n'.format(datetime.datetime.now().timestamp(), temperature, humidity)
    else:
        output = '{}, Failed to get reading'.format(datetime.datetime.now().timestamp())
    file = open('dht.log', 'a+')
    print(output)
    file.write(output)


def check_temp():
    if temperature > MAX_TEMP:
        print("Turning off temp")
        Energenie(2, initial_value=False)
    if temperature < MIN_TEMP:
        print("Turning on temp")
        Energenie(2, initial_value=True)


def check_humid():
    if humidity > MAX_HUMID:
        print("Turning off humid")
        Energenie(1, initial_value=False)
    if humidity < MIN_HUMID:
        print("Turning on humid")
        Energenie(1, initial_value=True)


while True:
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    write_to_file_and_sys()
    check_temp()
#     check_humid()
    time.sleep(FREQUENCY_SECONDS)
