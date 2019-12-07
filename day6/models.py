from __future__ import annotations


class CelestialBody:
    def __init__(self, name: str, parent: CelestialBody = None):
        self.name = name
        self.children = []
        self.parent = parent

    def __repr__(self):
        return f"<CelestialBody: {self.name}>"

    def add_child(self, child: CelestialBody):
        self.children.append(child)

    def get_all_child_orbits(self, parent_orbits: int = 0):

        if self.parent:
            parent_orbits += 1

        total_orbits = 0
        for child in self.children:
            total_orbits += child.get_all_child_orbits(parent_orbits)

        return total_orbits + parent_orbits
