import enum
from typing import List

from utils import load_input

intcode_program = load_input(raw=True)


class Opcode(enum.Enum):
    ADD = 1
    MULTIPLY = 2
    HALT = 99

    def __eq__(self, other):
        return self.value == other


def parse_intcode(program: str) -> List[int]:
    """Convert an intcode program into a list of ints.

    "1,2,3,4" -> [1, 2, 3, 4]
    """
    return [int(num) for num in program.split(",")]


def to_intcode(serialized_intcode: List[int]) -> str:
    """Turn a list of ints into an intcode program.

    [1, 2, 3, 4] -> "1,2,3,4"
    """
    return ",".join([str(num) for num in serialized_intcode])


def get_first_address(memory: str) -> int:
    """Get the first address in some intcode memory.

    "100,2,3,4" -> 100
    """
    return int(memory.split(",", 1)[0])


def run_intcode_program(program: str) -> str:
    """Computes the result of running the intcode.

    See the readme.md in this folder for more info on how this works.
    """
    instructions = parse_intcode(program)

    for index in range(0, len(instructions), 4):

        opcode = instructions[index]

        # If we encounter opcode 99, we're done.
        if opcode == Opcode.HALT:
            break

        # Initialize values
        first_index = instructions[index + 1]
        first_value = instructions[first_index]
        second_index = instructions[index + 2]
        second_value = instructions[second_index]
        target_index = instructions[index + 3]

        # Addition
        if opcode == Opcode.ADD:
            instructions[target_index] = first_value + second_value

        # Multiplication
        elif opcode == Opcode.MULTIPLY:
            instructions[target_index] = first_value * second_value

    return to_intcode(instructions)


# Restore the gravity assist program
parsed = parse_intcode(intcode_program)
parsed[1] = 12
parsed[2] = 2
intcode_program = to_intcode(parsed)

# Now run it through the computer
completed_program = run_intcode_program(intcode_program)
value = get_first_address(completed_program)
print(completed_program)
