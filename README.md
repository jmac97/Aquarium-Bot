# Aquarium Bot
A RPi powered device to monitor my friend's aquarium.

![Image of my son with the device](https://static.wixstatic.com/media/b6c492_c8d913bdd46f4f0b8f564870a7cf3da5~mv2_d_4032_3024_s_4_2.jpg/v1/fill/w_458,h_343,al_c,q_80,usm_0.66_1.00_0.01/77416181_475663866409673_198226640083563.webp)

## Introduction
I wanted to make a temperature monitor for my friend's aquarium that will allow her to receive daily updates and warnings if the temperature. So I did. The twitter account can be found [here](https://twitter.com/Soup19007731). Unfortunately, the new Stevens Media wifi setup will not recognize Pi Zeros (sad!) so it is currently out of commission, thus the inactive account.

Using the Twitter API, a Raspberry Pi, and a temperature sensor, the Aquarium Bot sends a daily tweet with a graph that shows the temperature changes over 24 hours. It will also send an SOS tweet if the tank temperature is too low or too high.

## Libraries & APIs
* You will need to setup a Twitter developer account. Setting up a separate Twitter account for this is ideal. Information can be found [here](https://developer.twitter.com/).
* os, time, RPi.GPIO as GPIO, twython import Twython, random, datetime, numpy as np, matplotlib.pyplot as plt, and math will need to be imported and installed onto the RPi
* Make sure to find your sensors output file (if you're receiving an error) and input the correct file path in line 41. Information about setting up the one-wire interface and setting them up can be found [here](https://www.raspberrypi-spy.co.uk/2018/02/enable-1-wire-interface-raspberry-pi/). 

## BOM
* Raspberry Pi Zero
* Blue LED
* Acrylic Sheet, to be laser cut into a box. File is name box.pdf.
* Bevel LED Holder 
* 4.7 kOhm Resistor
* Waterproof Temperature Sensor
