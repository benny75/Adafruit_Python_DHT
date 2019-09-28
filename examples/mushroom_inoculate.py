import time
import datetime
import Adafruit_DHT
from gpiozero import Energenie

FREQUENCY_SECONDS = 30
SENSOR = Adafruit_DHT.AM2302
PIN = 4

MIN_TEMP = 18
MAX_TEMP = 20

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
        if temp_on:
            print("Turning off temp")
        temp_on = False
        Energenie(1, initial_value=False)
    if temperature < MIN_TEMP:
        if not temp_on:
            print("Turning on temp")
        temp_on = True
        Energenie(1, initial_value=True)


while True:
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
    write_to_file_and_sys()
    check_temp()
    time.sleep(FREQUENCY_SECONDS)
