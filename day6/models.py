from __future__ import annotations

from typing import List


class CelestialBody:
    def __init__(self, name: str):
        self.name = name
        self.children = []
        self.parent = None

    def __repr__(self):
        return f"<CelestialBody: {self.name}>"

    def add_child(self, child: CelestialBody):
        self.children.append(child)

    def set_parent(self, parent: CelestialBody):
        self.parent = parent

    def get_all_child_orbits(self, parent_orbits: int = 0):

        if self.parent:
            parent_orbits += 1

        total_orbits = 0
        for child in self.children:
            total_orbits += child.get_all_child_orbits(parent_orbits)

        return total_orbits + parent_orbits

    def get_all_parents(self) -> List[CelestialBody]:
        body = self
        parents = []

        while True:
            if body.parent:
                body = body.parent
                parents.append(body)
            else:
                break

        return parents


class CelestialMapper:

    def __init__(self, orbital_chart: List[str]):
        self.orbital_chart = orbital_chart
        self.celestial_map = {}
        self.step_size = 20

    def map_celestial_objects(self):
        """Create all the objects and the relationships between them."""
        for orbit in self.orbital_chart:
            parent_name, child_name = orbit.split(")")
            parent = self.celestial_map.get(parent_name)
            child = self.celestial_map.get(child_name)

            # Check if we need to create the objects
            if parent_name not in self.celestial_map:
                parent = CelestialBody(name=parent_name)
                self.celestial_map[parent_name] = parent

            if child_name not in self.celestial_map:
                child = CelestialBody(name=child_name)
                self.celestial_map[child_name] = child

            # Create the relationship
            self.celestial_map[parent_name].add_child(child)
            self.celestial_map[child_name].set_parent(parent)

    def calculate_distance_between_bodies(self, origin: str, destination: str):
        """Calculate the number of orbital transfers needed to go from point A to point B"""

        # Find parents, we need distance between parents, not the bodies themselves.
        origin = self.celestial_map[origin]
        destination = self.celestial_map[destination]

        # Find all the parents,
        origin_parents = origin.get_all_parents()
        destination_parents = destination.get_all_parents()
        common_parents = set(origin_parents).intersection(set(destination_parents))

        # Figure out the nearest intersecting parent
        origin_index = min([origin_parents.index(parent) for parent in common_parents])
        nearest_parent = origin_parents[origin_index]
        destination_index = destination_parents.index(nearest_parent)

        # Now work out how far that is.
        return origin_index + destination_index





