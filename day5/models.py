import enum
from typing import List, Tuple, Union


class Opcode(enum.Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    HALT = 99

    def __eq__(self, other):
        return self.value == other


class ParameterMode(enum.Enum):
    POSITION_MODE = 0
    IMMEDIATE_MODE = 1

    def __eq__(self, other):
        return self.value == other


class IntcodeComputer:
    """Runs IntCode programs."""

    def __init__(self, program: str, start_state: Tuple[int, int]):
        self.step = 0
        self.memory = self._parse_intcode(program)

        # Restore the computer to a previous_state
        self.memory[1] = start_state[0]
        self.memory[2] = start_state[1]

    @staticmethod
    def _parse_intcode(program: str) -> List[int]:
        """Convert an intcode program into a list of ints.

        "1,2,3,4" -> [1, 2, 3, 4]
        """
        return [int(num) for num in program.split(",")]

    def get_first_address(self) -> int:
        """Get the first address in intcode memory.

        "100,2,3,4,2,500,99" -> 100
        """
        return self.memory[0]

    def get_value(self, value: int, parameter_mode: Union[int, ParameterMode]) -> int:
        """Get the value for a parameter."""
        if parameter_mode == ParameterMode.POSITION_MODE:
            return self.memory[value]
        elif parameter_mode == ParameterMode.IMMEDIATE_MODE:
            return value

    def run(self):
        """Run the IntCode program until we hit a HALT opcode."""
        while True:
            opcode = self.memory[self.step]

            if opcode == Opcode.HALT:
                break

            elif opcode == Opcode.ADD:
                first_param = self.get_value(self.memory[self.step + 1], ParameterMode.POSITION_MODE)
                second_param = self.get_value(self.memory[self.step + 2], ParameterMode.POSITION_MODE)
                target_index = self.memory[self.step + 3]
                self.memory[target_index] = first_param + second_param
                self.step += 4

            elif opcode == Opcode.MULTIPLY:
                first_param = self.get_value(self.memory[self.step + 1], ParameterMode.POSITION_MODE)
                second_param = self.get_value(self.memory[self.step + 2], ParameterMode.POSITION_MODE)
                target_index = self.memory[self.step + 3]
                self.memory[target_index] = first_param * second_param
                self.step += 4
