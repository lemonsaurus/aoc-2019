from typing import List, Tuple, Set

from bresenham import bresenham

from day3.star1 import get_wire_intersections, calculate_destination
from utils import load_input


def find_lowest_signal_decay(intersections: Set[Tuple[int, int]], *wires: List[List[str]]) -> int:
    """Find the intersection with the lowest signal decay.

    We do this in a very inefficient and straight forward way:
    For every intersection, simply run the wire until we get to that coordinate,
    keeping track of how many steps we've taken.
    """

    intersection_to_signal_decay = {}
    for intersection in intersections:
        signal_decay = 0
        for wire in wires:
            x, y = 0, 0

            for instruction in wire:
                # Calculate the destination and use bresenham to find all coords between the two points.
                destination = calculate_destination((x, y), instruction)
                intermediate_coords = list(bresenham(x, y, *destination))

                # Update the current coordinates
                x, y = destination

                # Check if the intersection is inside these intermediate coords
                if intersection in intermediate_coords:
                    signal_decay += intermediate_coords.index(intersection)
                    break
                else:
                    signal_decay += len(intermediate_coords) - 1

        intersection_to_signal_decay[str(intersection)] = signal_decay

    return min(intersection_to_signal_decay.values())


if __name__ == "__main__":
    # Load the input
    first_wire, second_wire = load_input()
    first_wire = first_wire.split(",")
    second_wire = second_wire.split(",")

    # Find the intersection with the least signal delay
    intersections = get_wire_intersections(first_wire, second_wire)
    print(find_lowest_signal_decay(intersections, first_wire, second_wire))
