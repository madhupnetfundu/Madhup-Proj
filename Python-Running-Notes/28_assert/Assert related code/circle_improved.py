#circle_improved.py
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("positive radius expected")
        self._radius = value

    def area(self):
        return math.pi * self.radius ** 2

    def correct_radius(self, correction_coefficient):
        self.radius *= correction_coefficient
