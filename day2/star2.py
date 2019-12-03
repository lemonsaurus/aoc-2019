from utils import load_input

from day2.star1 import run_intcode_program, get_first_address, parse_intcode, to_intcode

intcode_program = load_input(raw=True)
target = 19690720

for noun in range(100):
    for verb in range(100):

        # Print a progress indicator
        print(".", end="")

        # Reset memory and inject parameters
        parsed = parse_intcode(intcode_program)
        parsed[1] = noun
        parsed[2] = verb
        program = to_intcode(parsed)

        # Run the program
        completed_program = run_intcode_program(program)
        value = get_first_address(completed_program)

        # If we've hit the target, calculate the answer
        if value == target:
            print("-- Target hit! --")
            print(f"The answer is {100 * noun + verb}")
            exit()

