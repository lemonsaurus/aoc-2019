import enum
from typing import List, Tuple, Union, Optional


class Opcode(enum.Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
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

    def __init__(self, program: str, start_state: Optional[Tuple[int, int]] = None):
        self.pointer = 0
        self.memory = self._parse_program(program)

        # Restore the computer to a previous_state
        if start_state:
            self.memory[1] = start_state[0]
            self.memory[2] = start_state[1]

        # Address pointers
        self.opcode = None
        self.first_param = None
        self.second_param = None
        self.target_index = None

    @staticmethod
    def _parse_program(program: str) -> List[int]:
        """Convert an intcode program into a list of ints.

        "1,2,3,4" -> [1, 2, 3, 4]
        """
        return [int(num) for num in program.split(",")]

    def _get_value(self, value: int, parameter_mode: Union[int, ParameterMode]) -> int:
        """Get the value for a parameter."""
        if parameter_mode == ParameterMode.POSITION_MODE:
            return self.memory[value]
        elif parameter_mode == ParameterMode.IMMEDIATE_MODE:
            return value

    def get_first_address(self) -> int:
        """Get the first address in intcode memory.

        "100,2,3,4,2,500,99" -> 100
        """
        return self.memory[0]

    def _parse_instruction(self) -> None:
        """Parse the current instruction into its components."""

        # Parse and set the opcode
        opcode = self.memory[self.pointer]
        opstring = str(opcode).zfill(5)  # Pad with leading zeroes
        self.opcode = Opcode(int(opstring[-2:]))

        # Set the modes
        first_mode = int(opstring[-3])
        second_mode = int(opstring[-4])
        # third_mode = int(opstring[-5])

        # Set the params
        if self.opcode in (Opcode.ADD, Opcode.MULTIPLY, Opcode.LESS_THAN, Opcode.EQUALS):
            self.first_param = self._get_value(self.memory[self.pointer + 1], first_mode)
            self.second_param = self._get_value(self.memory[self.pointer + 2], second_mode)
            self.target_index = self.memory[self.pointer + 3]

        elif self.opcode == Opcode.INPUT or self.opcode == Opcode.OUTPUT:
            if first_mode == ParameterMode.POSITION_MODE:
                self.target_index = self.memory[self.pointer + 1]
            elif first_mode == ParameterMode.IMMEDIATE_MODE:
                self.target_index = self.pointer + 1

        elif self.opcode == Opcode.JUMP_IF_FALSE or self.opcode == Opcode.JUMP_IF_TRUE:
            self.first_param = self._get_value(self.memory[self.pointer + 1], first_mode)
            self.second_param = self._get_value(self.memory[self.pointer + 2], second_mode)

    def run(self):
        """Run the IntCode program until we hit a HALT opcode."""
        while True:
            self._parse_instruction()

            if self.opcode == Opcode.HALT:
                break

            elif self.opcode == Opcode.ADD:
                self.memory[self.target_index] = self.first_param + self.second_param
                self.pointer += 4

            elif self.opcode == Opcode.MULTIPLY:
                self.memory[self.target_index] = self.first_param * self.second_param
                self.pointer += 4

            elif self.opcode == Opcode.INPUT:
                input_value = input("Please input an intcode: ")
                self.memory[self.target_index] = int(input_value)
                self.pointer += 2

            elif self.opcode == Opcode.OUTPUT:
                print(self.memory[self.target_index])
                self.pointer += 2

            elif self.opcode == Opcode.JUMP_IF_TRUE:
                if self.first_param != 0:
                    self.pointer = self.second_param
                else:
                    self.pointer += 3

            elif self.opcode == Opcode.JUMP_IF_FALSE:
                if self.first_param == 0:
                    self.pointer = self.second_param
                else:
                    self.pointer += 3

            elif self.opcode == Opcode.LESS_THAN:
                if self.first_param < self.second_param:
                    self.memory[self.target_index] = 1
                else:
                    self.memory[self.target_index] = 0
                self.pointer += 4

            elif self.opcode == Opcode.EQUALS:
                if self.first_param == self.second_param:
                    self.memory[self.target_index] = 1
                else:
                    self.memory[self.target_index] = 0
                self.pointer += 4






