from typing import List, Tuple, Set

from bresenham import bresenham

from utils import load_input, get_manhattan_distance


def calculate_destination(origin: Tuple[int, int], instruction: str) -> Tuple[int, int]:
    """Calculate the destination by applying the instruction to the origin.

    For example, if the origin is 0,0 and the instruction is R50,
    this should return 0,50.
    """
    direction = instruction[0]
    distance = int(instruction[1:])
    x, y = origin

    if direction == "U":
        x += distance
    elif direction == "D":
        x -= distance
    elif direction == "R":
        y += distance
    elif direction == "L":
        y -= distance

    return x, y


def get_wire_intersections(*wires: List[List[str]]) -> Set[Tuple[int, int]]:
    """
    Calculate the manhattan distance to the closest intersection between
    the two wires described by the provided wiring diagrams.
    """

    wire_coords = []
    for wiring_diagram in wires:

        # Start at origin
        x, y = 0, 0

        # A set to store the coords in
        coordinates = set()

        for instruction in wiring_diagram:
            # Calculate the destination and use bresenham to find all coords between the two points.
            destination = calculate_destination((x, y), instruction)
            intermediate_coords = bresenham(x, y, *destination)

            # Update the current coordinates
            x, y = destination

            # Store the coords in the set
            coordinates.update(intermediate_coords)

        wire_coords.append(coordinates)

    # Now let's use intersection to figure out where the wires intersect.
    _intersections = wire_coords[0].intersection(wire_coords[1])

    # Ignore intersections at origin
    _intersections.remove((0, 0))

    return _intersections


if __name__ == "__main__":
    # Load the input
    first_wire, second_wire = load_input()
    first_wire = first_wire.split(",")
    second_wire = second_wire.split(",")

    # Calculate the closest wire cross
    intersections = get_wire_intersections(first_wire, second_wire)
    closest_intersection = min([get_manhattan_distance((0, 0), (x, y)) for x, y in intersections])
    print(closest_intersection)
