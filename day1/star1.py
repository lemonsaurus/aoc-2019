from utils import load_input

module_masses = load_input()
total_fuel_required = 0

for mass in module_masses:
    total_fuel_required += (int(mass) // 3) - 2

print("--- TOTAL FUEL REQUIREMENT CALCULATED ---")
print(f"The fuel required in total is {total_fuel_required}")
