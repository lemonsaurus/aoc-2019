import more_itertools

from day8.models import Pixel, PixelColor
from utils import load_input

encoded_image = load_input(raw=True)
previous_end = 0
decoded_image = [Pixel() for _ in range(150)]


def show_image() -> None:
    """Show the image as six rows of 25 pixels"""
    for row in more_itertools.chunked(decoded_image, 25):
        stringified = [str(pixel) for pixel in row]
        print("".join(stringified))


# Iterate through the image 150 pixels at a time
for layer in more_itertools.chunked(encoded_image, 150):

    # Iterate through the pixels and store them if they're not transparent.
    for i, pixel_value in enumerate(layer):
        pixel_color = PixelColor(int(pixel_value))

        if pixel_color != PixelColor.TRANSPARENT and decoded_image[i].value is None:
            decoded_image[i] = Pixel(pixel_color)

show_image()
