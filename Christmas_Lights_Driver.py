import time
import board
import neopixel  # The special library to drive the RGB LEDs.
import random

# The RPi Board-pin connected to the DATA-in of the RGB light strand.
pixel_pin = board.D21

# The number of pixels on the light strand.
num_pixels = 50

# The order of the pixel colors - RGB vs. GRB.
ORDER = neopixel.RGB

# class neopixel.NeoPixel(pin: microcontroller.Pin,
#                         n: int,
#                         bpp (bytes per pixel): int = 3,
#                         brightness: float = 1.0,
#                         auto_write: bool = True,
#                         pixel_order: str = None)
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False, pixel_order=ORDER)

# Dictionary of standard color-name(key), RGB color-code(value) pairs.
color_dict = {
      'red'   : (255, 0, 0),
      'orange': (229, 83, 0),
      'yellow': (249, 199, 28),
      'green' : (0, 255, 0),
      'blue'  : (0, 0, 255),
      'indigo': (75, 0, 130),
      'violet': (143, 0, 255),
      'white' : (255, 255, 255),
      'pink'  : (255, 20, 147),
      'ballet': (255, 20, 147),
      'aqua'  : (127, 255, 212),
      'butter': (249, 199, 28),
      'peach' : (229, 83, 0),
      'cyan'  : (0, 255, 239),
      'off'   : (0, 0, 0)
}

# Dictionary of letters(key), pixel-number(value) pairs.
letter_light_dict = {
    'Z': 0,
    'Y': 1,
    'X': 3,
    'W': 5,
    'V': 7,
    'U': 8,
    'T': 9,
    'S': 11,
    'R': 30,
    'Q': 29,
    'P': 27,
    'O': 26,
    'N': 24,
    'M': 22,
    'L': 21,
    'K': 19,
    'J': 18,
    'I': 34,
    'H': 39,
    'G': 40,
    'F': 41,
    'E': 42,
    'D': 44,
    'C': 46,
    'B': 47,
    'A': 49,
}
# test function to verify all lights are operational.
def test():
    print ("Test...")
    pixels.fill(color_dict['cyan'])
    pixels.show()

# christmas_pattern sets the default christmas color pattern across all lights.
def christmas_pattern():
    print ("Christmas Pattern...")
    pixels[0] = color_dict['red']
    pixels[1] = color_dict['orange']
    pixels[2] = color_dict['yellow']
    pixels[3] = color_dict['green']
    pixels[4] = color_dict['blue']
    pixels[5] = color_dict['red']
    pixels[6] = color_dict['orange']
    pixels[7] = color_dict['yellow']
    pixels[8] = color_dict['green']
    pixels[9] = color_dict['blue']
    pixels[10] = color_dict['red']
    pixels[11] = color_dict['orange']
    pixels[12] = color_dict['yellow']
    pixels[13] = color_dict['green']
    pixels[14] = color_dict['blue']
    pixels[15] = color_dict['red']
    pixels[16] = color_dict['orange']
    pixels[17] = color_dict['yellow']
    pixels[18] = color_dict['green']
    pixels[19] = color_dict['blue']
    pixels[20] = color_dict['red']
    pixels[21] = color_dict['orange']
    pixels[22] = color_dict['yellow']
    pixels[23] = color_dict['green']
    pixels[24] = color_dict['blue']
    pixels[25] = color_dict['red']
    pixels[26] = color_dict['orange']
    pixels[27] = color_dict['yellow']
    pixels[28] = color_dict['green']
    pixels[29] = color_dict['blue']
    pixels[30] = color_dict['red']
    pixels[31] = color_dict['orange']
    pixels[32] = color_dict['yellow']
    pixels[33] = color_dict['green']
    pixels[34] = color_dict['blue']
    pixels[35] = color_dict['red']
    pixels[36] = color_dict['orange']
    pixels[37] = color_dict['yellow']
    pixels[38] = color_dict['green']
    pixels[39] = color_dict['blue']
    pixels[40] = color_dict['red']
    pixels[41] = color_dict['orange']
    pixels[42] = color_dict['yellow']
    pixels[43] = color_dict['green']
    pixels[44] = color_dict['blue']
    pixels[45] = color_dict['red']
    pixels[46] = color_dict['orange']
    pixels[47] = color_dict['yellow']
    pixels[48] = color_dict['green']
    pixels[49] = color_dict['blue']
    pixels.show()

# stranger_things_pattern displays a sequence spelling the user's input string with a flickering lights finish.
def stranger_things_pattern(input_string):
    print ("Stranger Things Pattern...")
    pattern_string = input_string.upper()
    color_list = ['red', 'orange', 'yellow', 'green', 'blue']

    # Initialize the lights to christmas lights pattern.
    christmas_pattern()
    time.sleep(2)
    pixels.fill(color_dict['off'])
    pixels.show()
    time.sleep(2)

    # Logic that takes the individual letter in a string, finds the matching pixel number in letter_light_dict
    # and turns on the corresponding light. Iterate through entire string.
    for letter in pattern_string:
        if letter == ' ':
            time.sleep(2.2)
            continue
        pixel_number = letter_light_dict.get(letter)
        color = random.choice(color_list)
        pixels[pixel_number] = color_dict[color]
        pixels.show()
        time.sleep(1.2)
        pixels[pixel_number] = color_dict['off']
        pixels.show()

    # Perform a red terror pattern
    for i in range(5):
        pixels.fill(color_dict['red'])
        pixels.show()
        time.sleep(0.08)
        pixels.fill(color_dict['off'])
        pixels.show()
        time.sleep(0.08)

# christmas_even_pattern turns alternating lights on and off in a christmas color pattern.
def christmas_even_pattern(wait):
    print ("Christmas Even Pattern...")
    pixels[0] = color_dict['red']
    pixels[1] = color_dict['off']
    pixels[2] = color_dict['yellow']
    pixels[3] = color_dict['off']
    pixels[4] = color_dict['blue']
    pixels[5] = color_dict['off']
    pixels[6] = color_dict['orange']
    pixels[7] = color_dict['off']
    pixels[8] = color_dict['green']
    pixels[9] = color_dict['off']
    pixels[10] = color_dict['red']
    pixels[11] = color_dict['off']
    pixels[12] = color_dict['yellow']
    pixels[13] = color_dict['off']
    pixels[14] = color_dict['blue']
    pixels[15] = color_dict['off']
    pixels[16] = color_dict['orange']
    pixels[17] = color_dict['off']
    pixels[18] = color_dict['green']
    pixels[19] = color_dict['off']
    pixels[20] = color_dict['red']
    pixels[21] = color_dict['off']
    pixels[22] = color_dict['yellow']
    pixels[23] = color_dict['off']
    pixels[24] = color_dict['blue']
    pixels[25] = color_dict['off']
    pixels[26] = color_dict['orange']
    pixels[27] = color_dict['off']
    pixels[28] = color_dict['green']
    pixels[29] = color_dict['off']
    pixels[30] = color_dict['red']
    pixels[31] = color_dict['off']
    pixels[32] = color_dict['yellow']
    pixels[33] = color_dict['off']
    pixels[34] = color_dict['blue']
    pixels[35] = color_dict['off']
    pixels[36] = color_dict['orange']
    pixels[37] = color_dict['off']
    pixels[38] = color_dict['green']
    pixels[39] = color_dict['off']
    pixels[40] = color_dict['red']
    pixels[41] = color_dict['off']
    pixels[42] = color_dict['yellow']
    pixels[43] = color_dict['off']
    pixels[44] = color_dict['blue']
    pixels[45] = color_dict['off']
    pixels[46] = color_dict['orange']
    pixels[47] = color_dict['off']
    pixels[48] = color_dict['green']
    pixels[49] = color_dict['off']
    pixels.show()
    time.sleep(wait)

    pixels[0] = color_dict['off']
    pixels[1] = color_dict['orange']
    pixels[2] = color_dict['off']
    pixels[3] = color_dict['green']
    pixels[4] = color_dict['off']
    pixels[5] = color_dict['red']
    pixels[6] = color_dict['off']
    pixels[7] = color_dict['yellow']
    pixels[8] = color_dict['off']
    pixels[9] = color_dict['blue']
    pixels[10] = color_dict['off']
    pixels[11] = color_dict['orange']
    pixels[12] = color_dict['off']
    pixels[13] = color_dict['green']
    pixels[14] = color_dict['off']
    pixels[15] = color_dict['red']
    pixels[16] = color_dict['off']
    pixels[17] = color_dict['yellow']
    pixels[18] = color_dict['off']
    pixels[19] = color_dict['blue']
    pixels[20] = color_dict['off']
    pixels[21] = color_dict['orange']
    pixels[22] = color_dict['off']
    pixels[23] = color_dict['green']
    pixels[24] = color_dict['off']
    pixels[25] = color_dict['red']
    pixels[26] = color_dict['off']
    pixels[27] = color_dict['yellow']
    pixels[28] = color_dict['off']
    pixels[29] = color_dict['blue']
    pixels[30] = color_dict['off']
    pixels[31] = color_dict['orange']
    pixels[32] = color_dict['off']
    pixels[33] = color_dict['green']
    pixels[34] = color_dict['off']
    pixels[35] = color_dict['red']
    pixels[36] = color_dict['off']
    pixels[37] = color_dict['yellow']
    pixels[38] = color_dict['off']
    pixels[39] = color_dict['blue']
    pixels[40] = color_dict['off']
    pixels[41] = color_dict['orange']
    pixels[42] = color_dict['off']
    pixels[43] = color_dict['green']
    pixels[44] = color_dict['off']
    pixels[45] = color_dict['red']
    pixels[46] = color_dict['off']
    pixels[47] = color_dict['yellow']
    pixels[48] = color_dict['off']
    pixels[49] = color_dict['blue']
    pixels.show()
    time.sleep(wait)

try:
    while True:
        # Performs a continuous lightshow of patterns based on our functions.
        for i in range(20):
            christmas_even_pattern(1)
        christmas_pattern()
        time.sleep(5)
        stranger_things_pattern("RIGHT HERE RUN")
        christmas_pattern()
        time.sleep(5)
finally:
    pixels.deinit()  # De-initialize the LED pixels.


