# Macro Pad

This is the software I'm using for a simple Macro Pad based on the Pi Pico.  Using this software is pretty straight forward. I design a parametric enclosure for it. It can be found at http://......

1. Install Circuit Python.  

    There are many excellent tutorials about it on the web.  

    You can download Circuit Python at `https://circuitpython.org/downloads`

    Mainly, press and hold the boot button and plug your Pi Pico on your computer.  After a few seconds,  release then boot button.  A drive will appear on your computer.  Copy the Circuit Python firmware onto the drive.  The Pi Pico will reboot by itself.  A new drive will appear named `CIRCUITPY`. You should be good to go.

    The Circuit Python firmware I use have the file name `adafruit-circuitpython-raspberry_pi_pico-en_US-9.2.8.uf2`.

1. Install an IDE like Thonny.

1. Install the Macro Pad software.

    Copy the files of this project in the `CIRCUITPY` drive.  The library dependencies are included.  If you want the firmware to start automatically, rename the file `macro_pad_firmware.py` to `code.py`.

1. Configure the Macro Pad software.  Open the file key_definitions.py and customize it.

    1. Remove or add keys as you wish.  Make sure that the indices starts from zero and are consecutive up to the last one.
    1. Set the GPIO pin that each key uses.  The io_pin must be a Pi Pico GPIO pin from the board library, such as board.GPIO5. The order the GPIOs are listed is irrelevant. The GPIO will output the corresponding macro.
    1. Set the macro for each key.  A macro is a list of macro components.  A macro component can be:
        1. A string, such as 'This is a string\n'.  It can contain Python Escape Characters such as \n for newline, and so on.
        1. A single keycode from the keycode library such as Keycode.ONE, Keycode.A, and so on.  Some of them can be found on `https://docs.circuitpython.org/projects/hid/en/latest/api.html`
        1. A list of keycodes from the keycode library between parentheses (tuple).  They will be sent out as if they were all pressed together.  (Keycode.SHIFT, Keycode.ONE) will output a ! for a US keyboard. 

1. Restart your Pi Pico to reload the key_definitions.py file.

This is the first version of the software.  I will improve it based on my usage and comments I will receive.
