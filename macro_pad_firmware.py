######################################################################################
#
# Pi Pico based macro pad key firmware using Circuit Python
#
######################################################################################
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHOR OR COPYRIGHT
# HOLDER BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# IT IS NOT PERMITTED TO MODIFY THIS COMMENT BLOCK.
#
# (c)2025, Claude "Tryphon" Theroux, Montreal, Quebec, Canada
# http://www.ctheroux.com/
#
######################################################################################

######################################################################################
#
# In order to use this software, you will need to install Circuit Python and copy the
# library adafruit_hid into the lib directory of the Pi Pico.  The adafruit_hid can be
# found at https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/latest in
# the lib directory. Use the version that relates to you Circuit Python version.

import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import board
import digitalio
from array import *
from key_definitions import key_definitions
import json

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

# Initialize the GPIOs for every key.
def initialize_gpio(key_definitions):
    
    pin_handles = list()
    
    for index in key_definitions:
        pin = digitalio.DigitalInOut(key_definitions[index]['io_pin'])
        pin.direction = digitalio.Direction.INPUT
        pin.pull = digitalio.Pull.UP
        pin_handles.append(pin)
        
    return pin_handles

# Perform the macro when a given key is pressed.
def run_key_macro(keyboard, keyboard_layout, key):
    print(key)
    if len(key) == 0:
        return
    for macro_component in key['macro']:
        if type(macro_component) == int:
            keyboard.send(macro_component)
        elif type(macro_component) == str:
            keyboard_layout.write(macro_component)
        elif type(macro_component) == tuple:
            for component in macro_component:
                keyboard.press(component)
            keyboard.release_all()
        else:
            print('Unsupported macro component type ' + str(type(macro_component)))
   
pin_handles = initialize_gpio(key_definitions)

while True:
    for index in range(len(pin_handles)):
        if not pin_handles[index].value:
            run_key_macro(keyboard, keyboard_layout, key_definitions[index])
            time.sleep(0.2)
            
