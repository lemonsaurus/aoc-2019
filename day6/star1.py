from day6.models import CelestialBody
from utils import load_input

orbital_chart = load_input()
celestial_objects = {}

for orbit in orbital_chart:
    parent, child = orbit.split(")")

    # Check if we need to create the objects
    if parent not in celestial_objects:
        parent_body = CelestialBody(name=parent)
        celestial_objects[parent] = parent_body

    if child not in celestial_objects:
        child_body = CelestialBody(name=child, parent=celestial_objects[parent])
        celestial_objects[child] = child_body

    # Create the relationship
    celestial_objects[parent].add_child(celestial_objects[child])

print(celestial_objects["COM"].get_all_child_orbits())
