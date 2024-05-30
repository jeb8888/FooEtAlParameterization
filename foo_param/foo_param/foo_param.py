# Foo et al. Parameterization Package
# Written by Jared Ebenstein
# May 29, 2024
# For UCAR

import math

class FooParameterization:
    def __init__(self, radius):
        self.radius = radius

    def validate(self):
        if self.radius <= 0:
            raise ValueError("Radius must be a positive number")

    def calculate_volume(self):
        """Uses Foo et al. parameterization to take the radius of a sphere and return its volume"""
        volume = (4 / 3) * math.pi * self.radius ** 3
        return volume


if __name__ == "__main__":
    param = FooParameterization(5)
    param.validate()
    volume = param.calculate_volume()
    print(f"Volume: {volume}")