#Main Program
#some of these imports will fail on pylint
#they are specifically for raspberry pi
# pylint: disable-all

import adafruit_dht
import board
import csv
import datetime
import LCD
import psutil
import time



while True:
    for proc in psutil.process_iter():
        if proc.name() == 'libgpiod_pulseIn' or proc.name() == 'libgpiod_pulse1':
            proc.kill()

    TEMPERATURE = None
    HUMIDITY = None
    while True:
        try:
            print("reading sensor")
            sensor = adafruit_dht.DHT11(board.D24)
            TEMPERATURE = sensor.TEMPERATURE
            HUMIDITY = sensor.HUMIDITY
            break
        except RuntimeError as error:
            print(error.args[0])
            print("error 1")
            time.sleep(2.0)
            for proc in psutil.process_iter():
                if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulse1':
                    proc.kill()
        except Exception as error:
            sensor.exit()
            print("error 2")
            raise error

        if HUMIDITY is not None and TEMPERATURE is not None:
            lcd = LCD()
            #we first check if a libgpiod process is running. If yes, we kill it!
            with open("test2.csv", 'a', newline='') as file:
                #time info
                todays_date = datetime.datetime.now().strftime("%A, %d, %b, %y")
                local_time = time.localtime()
                current_time = time.strftime("%H:%M:%S", local_time)
                today = current_time + todays_date

                #Evaluate the TEMPERATURE and HUMIDITY STATUS
                if 20 <= TEMPERATURE <= 21:
                    TEMPERATURE_STATUS = "Good"
                else:
                    #If this is the case we need to send a message to the customer
                    TEMPERATURE_STATUS = "Bad"

                if 68 <= HUMIDITY <= 74:
                    HUMIDITY_STATUS = "Good"
                else:
                    #If this is the case we need to send a message to the customer
                    HUMIDITY_STATUS = "Bad"

                writer = csv.writer(file)
                writer.writerow([today, TEMPERATURE, TEMPERATURE_STATUS, HUMIDITY, HUMIDITY_STATUS])
                led = LCD()
                lcd.clear()
                lcd.text(f'Temp: C % {TEMPERATURE}')
                lcd.text(f'humidity: C % {HUMIDITY}')
