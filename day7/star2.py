import itertools

from models import IntcodeComputer
from utils import load_input

amplifier_program = load_input(raw=True)
signal_permutations = itertools.permutations(range(5, 10), 5)
thruster_signals = []

for permutation in signal_permutations:
    amp_output = 0
    amplifiers = {}

    # Create all the computers
    for phase_setting in permutation:
        amplifiers[phase_setting] = IntcodeComputer(
            program=amplifier_program,
            input_values=[phase_setting]
        )

    # Keep cycling through the phase settings until the programs are complete
    for phase_setting in itertools.cycle(permutation):
        amplifier = amplifiers[phase_setting]

        # If this amp has halted, check if we should stop iterating.
        if amplifier.halted:
            if all([amp.halted for amp in amplifiers.values()]):
                break
            continue

        amplifier.input_values.appendleft(amp_output)
        amplifier.run(pause_after_output=True)
        if amplifier.output_values:
            amp_output = amplifier.output_values.pop()

    thruster_signals.append(amp_output)

print(max(thruster_signals))
