from models import IntcodeComputer
from utils import load_input

intcode_program = load_input(raw=True)

computer = IntcodeComputer(intcode_program)
computer.run()
