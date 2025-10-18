import math


class Shape:
    """Base shape class declaring area() to be implemented by subclasses."""

    def area(self):
        """Return the area of the shape.

        Subclasses must override this method.
        """
        raise NotImplementedError("Subclasses must implement area()")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


def print_area(shape: shape)
