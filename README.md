# ESP32 Webserver

### What Is It?
We are creating a minimal web server using built-in micropython libraries.

We will be using esptool.py for installing micropython.

We will be using adafruits ampy tool for interacting with the board.

You will need your own serial monitor like the arduino IDE, Screen (MacOS), or PuTTY.

### Get Started:
Clone The Repo:

`git clone https://github.com/davissanders/esp32-webserver.git`

Set up python virtual environment with venv or pyenv (Don't forget to activate it)

Install the reqirements: `pip install -r requirements.txt`

Make sure the esp32 board is connected and powered on (You will see a red LED)

### Installation
First you need to find the serial port of your board. To do this reference the [espressif docs](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/establish-serial-connection.html)

Install micropython framework to the esp32 (this might take a minute or so): 

`esptool.py --chip esp32 --port /dev/cu.usbserial-0001 --baud 115200 write_flash -z 0x1000 esp32-20210902-v1.17.bin`

To check this worked, we will use ampy to see what files are on the board:

`ampy -p <board serial port> ls` (this should show /boot.py)

Now we need to remove boot.py from the board and install our own boot.py file:

`ampy -p /dev/cu.usbserial-0001 rm boot.py`

Edit your boot.py file and add your network ssid and password. Then we add them to the board:

`ampy -p /dev/cu.usbserial-0001 put boot.py`

`ampy -p /dev/cu.usbserial-0001 put main.py`

### Start It Up!
Once this is done, you are ready to go! 
Open a serial monitor connection and then press the 'EN' button on your esp32.
You will get a printout of the esp32 ip address which you will use to connect.
