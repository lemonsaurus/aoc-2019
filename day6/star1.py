from day6.models import CelestialMapper
from utils import load_input

orbital_chart = load_input()
mapper = CelestialMapper(orbital_chart)
mapper.map_celestial_objects()
total_orbits = mapper.celestial_map['COM'].get_all_child_orbits()

print(total_orbits)
