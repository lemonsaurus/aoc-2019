import string
from typing import Union

ALLOWED_CHARS = string.ascii_lowercase + string.ascii_uppercase
MAXCHAR_LIMIT = len(ALLOWED_CHARS)


def load_input(input_file: str = "input.txt", raw: bool = False) -> Union[list, str]:
    """Load the input data into memory."""
    with open(input_file, "r") as readfile:

        if not raw:
            return readfile.read().strip().split("\n")
        else:
            return readfile.read()


def _increment_symbol(letter: str) -> str:
    """
    This helper function increments a symbol.
    increment_symbol('a') -> 'b'
    increment_symbol('z') -> 'A'
    increment_symbol('9') -> 'a'
    """
    return ALLOWED_CHARS[
        (ALLOWED_CHARS.find(letter) + 1) % MAXCHAR_LIMIT
    ]


def next_short_string(prev_string: str = None) -> str:
    """
    This function generates a short string
    and returns it to the user.

    If a previous string is provided,
    it returns the next in the series.

    If a list of protected strings is provided,
    it will recursively generate new strings until
    it finds a string that is not in that list.

    Allowed characters are a-z and A-Z (in that order)
    next_short_string('a')      -> 'b'
    next_short_string('abz')    -> 'abA'
    next_short_string('9')      -> 'aa'
    next_short_string('aBCf99') -> 'aCDgaa'
    next_short_string('9999')   -> 'aaaaa'

    Please don't judge, I wrote this years ago for a
    URL shortener and am just reusing it for this.
    """

    # if no prev_string was provided, we'll just start at 'a'
    if not prev_string:
        return 'a'

    # make the string a list so it'll be mutable
    new_string = list(prev_string)

    # iterate through the list backwards
    for num, symbol in enumerate(reversed(list(prev_string))):

        # always increment the last symbol
        if num + 1 == len(prev_string):
            new_string[num] = _increment_symbol(symbol)

            # if that was the only symbol and it turned into an 'a', we gotta add another 'a' to the end.
            if num == 0 and new_string[num] == 'a':
                new_string.append('a')

        # if the previous symbol was incremented to 'a', keep incrementing
        elif new_string[num + 1] == 'a':
            new_string[num] = _increment_symbol(symbol)

            # if the first symbol just turned into an 'a', we have to add another 'a' to the end
            if num == 0 and new_string[num] == 'a':
                new_string.append('a')

        # if the previous symbol didn't turn into 'a', we don't need to keep going.
        else:
            break

    # put it back together
    new_string = ''.join(new_string)
    return new_string


def get_manhattan_distance(a, b):
    """
    Finds the manhattan distance between
    point a and point b
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
