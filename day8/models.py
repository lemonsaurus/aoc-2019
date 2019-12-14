import enum


class ValueTracker:
    fewest_zeroes = None
    number_of_ones = None
    number_of_twos = None


class PixelColor(enum.Enum):
    BLACK = 0
    WHITE = 1
    TRANSPARENT = 2


class Pixel:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        if self.value == PixelColor.WHITE:
            return "█"
        return "░"
