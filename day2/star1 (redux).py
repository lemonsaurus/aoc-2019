from utils import load_input

from models import IntcodeComputer

intcode_program = load_input(raw=True)

computer = IntcodeComputer(
    intcode_program,
    (12, 2)
)
computer.run()
print(computer.get_first_address())
