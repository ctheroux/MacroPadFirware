######################################################################################
#
# Pi Pico based macro pad key definitions
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
 
import board
from adafruit_hid.keycode import Keycode

# Remove or add keys as you wish:24,36you.  Make sure that the indices starts from zero and are
# consecutive up to the last one.
#
# The io_pin must be a Pi Pico GPIO pin from the board library, such as board.GPIO5.
# The order the GPIOs are listed is irrelevant. The GPIO will output the corresponding
# macro.
#
# The macro is a list of macro components.  They can be:
# - A string, such as "This is a string\n"
# - A single keycode from the keycode library such as Keycode.ONE, Keycode.A.
# - A list of keycodes from the keycode library between parentheses (tuple).  They will
#   be sent out as if they were all pressed together.  (Keycode.SHIFT, Keycode.ONE) will
#   output ! for a US keyboard. 

key_definitions = {
    
    0: 	{
            'io_pin': board.GP5,
            'macro': [ 'a string\n', Keycode.ONE, (Keycode.SHIFT, Keycode.ONE) ]
        },
    1: 	{
            'io_pin': board.GP4,
            'macro': []
        },
    2: 	{
            'io_pin': board.GP3,
            'macro': []
        },
    3: 	{
            'io_pin': board.GP2,
            'macro': []
        },
    4: 	{
            'io_pin': board.GP6,
            'macro': []
        },
    5: 	{
            'io_pin': board.GP7,
            'macro': []
        },
    6: 	{
            'io_pin': board.GP8,
            'macro': []
        },
    7: 	{
            'io_pin': board.GP9,
            'macro': []
        },
    8: 	{
            'io_pin': board.GP10,
            'macro': []
        },
    9: 	{
            'io_pin': board.GP11,
            'macro': []
        },
    10: {
            'io_pin': board.GP12,
            'macro': []
        },
    11: {
            'io_pin': board.GP13,
            'macro': []
        },
    12: {
            'io_pin': board.GP14,
            'macro': []
        },
    13: {
            'io_pin': board.GP15,
            'macro': []
        },
    14: {
            'io_pin': board.GP17,
            'macro': []
        },
    15: {
            'io_pin': board.GP16,
            'macro': []
        }    
}
