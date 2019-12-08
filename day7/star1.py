import itertools

from models import IntcodeComputer
from utils import load_input

amplifier_program = load_input(raw=True)

signal_permutations = itertools.permutations(range(5), 5)

thruster_signals = []
for permutation in signal_permutations:
    amp_output = 0
    for phase_setting in permutation:
        computer = IntcodeComputer(
            program=amplifier_program,
            input_values=[amp_output, phase_setting]
        )
        computer.run()
        amp_output = computer.output_values[0]

    thruster_signals.append(amp_output)

print(max(thruster_signals))
