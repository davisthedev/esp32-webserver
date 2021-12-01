# We use the built in socket library to handle connections
try:
  import usocket as socket
except:
  import socket

# Pin allows us to manipulate the onboard LED
from machine import Pin

# network allows us to connect the esp32 to a wifi network
import network

# This just disables debugging messages
import esp
esp.osdebug(None)

# gc is the garbage collector, it handles reclaiming memory. Very important for microcontrollers with limited memory.
import gc
gc.collect()

# add network ssid and password. Don't commit them. I know it should be an ini or env
ssid = ''
password = ''

# Set the esp32 as a wifi station so it can recieve connections
station = network.WLAN(network.STA_IF)

# Activates the station and connects to our wifi network
station.active(True)
station.connect(ssid, password)

# Safety code to make sure the program does not run if you are not connected to wifi
while station.isconnected() == False:
  pass

# Prints the esp32 ip address for you
print('Connection successful')
print(station.ifconfig())

# Sets a variable for us to manipulate the onboard LED
led = Pin(2, Pin.OUT)
