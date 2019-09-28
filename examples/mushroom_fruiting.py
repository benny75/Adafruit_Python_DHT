
import time
import datetime
import Adafruit_DHT
from gpiozero import Energenie

FREQUENCY_SECONDS = 30
SENSOR = Adafruit_DHT.AM2302
PIN = 4


MIN_TEMP = 13
MAX_TEMP = 20
MIN_HUMID = 80
MAX_HUMID = 90

humid_count = 0
temp_on = False

def write_to_file_and_sys():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if humidity is not None and temperature is not None:
        output = '{}, {:.2f}, {:.2f}, {}\n'.format(now, temperature, humidity, temp_on)
    else:
        output = '{}, Failed to get reading'.format(now)
    file = open('dht.log', 'a+')
    print(output)
    file.write(output)
    file.close()


def check_temp():
    global temp_on
    if temperature > MAX_TEMP:
        print("Turning off temp")
        temp_on = False
        Energenie(2, initial_value=False)
    if temperature < MIN_TEMP:
        print("Turning on temp")
        temp_on = True
        Energenie(2, initial_value=True)


def check_humid():
    if humidity > MAX_HUMID:
        print("Turning off humid")
        Energenie(1, initial_value=False)
    if humidity < MIN_HUMID:
        print("Turning on humid")
        Energenie(1, initial_value=True)

def fruiting_humid():
    global humid_count
    if humid_count % 120 == 0:
        print("Turning on humid")
        Energenie(1, initial_value=True)
    elif humid_count % 120 == 2:
        print("Turning off humid")
        Energenie(1, initial_value=False)
        
    humid_count = humid_count + 1

while True:
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    write_to_file_and_sys()
#    check_temp()
    fruiting_humid()
#   check_humid()
    time.sleep(FREQUENCY_SECONDS)
