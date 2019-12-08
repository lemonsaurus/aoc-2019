from day6.models import CelestialMapper
from utils import load_input

orbital_chart = load_input()
mapper = CelestialMapper(orbital_chart)
mapper.map_celestial_objects()
distance_to_santa = mapper.calculate_distance_between_bodies("YOU", "SAN")

print(distance_to_santa)
