import os
import time
import RPi.GPIO as GPIO
from twython import Twython

from auth import (
  consumer_key,
  consumer_secret,
  access_token,
  access_token_secret
)

twitter = Twython (
  consumer_key,
  consumer_secret,
  access_token,
  access_token_secret
)

# Sets GPIO naming convention
GPIO.setmode(GPIO.BCM)

# Python won't print GPIO warnings to the screen
GPIO.setwarnings(False)

# Sets GPIO 18 as output
GPIO.setup(18,GPIO.OUT)

# RPi has a bunch of drivers but loading them all isn't feasable
# modprobe boots certain drivers when needed
# Next two lines boots 1-wire and thermometer drivers on GPIO 4
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# Define sensor's output file (w1_slave file)
temp_sensor = '/sys/bus/w1/devices/28-000008a86621/w1_slave'

# Open, read, record and then close temperature file
# This gets the raw temperature reading                                                                                 def read_temp_raw():
  f = open(temp_sensor, 'r')
  lines = f.readlines()
  f.close()
  return lines

# Getting the temperature from the raw temp
# Raw temp reading outputs two lines of data
# This reads and processes it
def read_temp():
  lines = read_temp_raw()  # Get the lines from raw temp
   # Takes the first of two lines and strips it of all characters except the last three
  # If the last three characters are 'YES' then there is no error from the reading
  while lines[0].strip()[-3:] != 'YES':

    # If there is an error, aka the last characters don't equal 'YES', then sleep for .2s and repeat
    time.sleep(0.2)
    lines = read_temp_raw()

  # If there's no error, go to the second of two lines and find 't=1' in the line
  temp_output = lines[1].find('t=')

  # If there's no errors, aka the above does not equal -1, then run calculations
  if temp_output != -1:
         # Strip the output of the 't=' phrase to leave just the temperature numbers
    temp_string = lines[1].strip()[temp_output+2:]

    # Calculate the temperature in C
    temp_c = float(temp_string) / 1000.0

    # Calculate the temperature in F
    temp_f = temp_c * 9.0 / 5.0 + 32.0

    if (temp_f >= 68):
      GPIO.output(18, GPIO.HIGH)
      message = "Fish test"
            twitter.update_status(status=message)
      print("Tweeted: %s" % message)
    else:
      GPIO.output(18, GPIO.LOW)
    # Return the temperature in F
    return temp_f

# Print the temp_f value then sleep for 1s
while True:
  print(read_temp())
  time.sleep(1)
