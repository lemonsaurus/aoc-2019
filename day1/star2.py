from utils import load_input

module_masses = load_input()


def _calculate_fuel_needed(mass):
    """Figure out how much fuel is needed for an amount of mass."""
    return (int(mass) // 3) - 2


def calculate_total_fuel_needed(mass):
    """Figure out the total fuel needed for an amount of mass, including fuel to carry the fuel."""
    fuel_required = _calculate_fuel_needed(mass)

    if _calculate_fuel_needed(fuel_required) <= 0:
        return fuel_required
    else:
        return fuel_required + calculate_total_fuel_needed(fuel_required)


total_fuel_required = 0
for mass in module_masses:
    total_fuel_required += calculate_total_fuel_needed(mass)

print("--- TOTAL FUEL REQUIREMENT CALCULATED ---")
print(f"The fuel required in total is {total_fuel_required}")
