from models import IntcodeComputer
from utils import load_input

intcode_program = load_input(raw=True)

computer = IntcodeComputer(intcode_program, input_values=[2])
computer.run(silence_output=False)

