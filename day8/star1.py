import more_itertools

from day8.models import ValueTracker
from utils import load_input

encoded_image = load_input(raw=True)  # Remove the \n
value_tracker = ValueTracker()

# Iterate through the image 150 pixels at a time
for layer in more_itertools.chunked(encoded_image, 150):

    # If this has less zeroes than a previously lowest one, store the other counts.
    zeroes = layer.count("0")
    if value_tracker.fewest_zeroes is None or zeroes < value_tracker.fewest_zeroes:
        value_tracker.fewest_zeroes = zeroes
        value_tracker.number_of_ones = layer.count("1")
        value_tracker.number_of_twos = layer.count("2")

print(value_tracker.number_of_ones * value_tracker.number_of_twos)
