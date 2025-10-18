import math


class Shape:
    """Base shape class declaring area() to be implemented by subclasses."""

    def area(self):
        """Return the area of the shape.

        Subclasses must override this method.
        """
        raise NotImplementedError("Subclasses must implement area()")


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


def print_area(shape: Shape):
    """Print the area for a Shape instance."""
    print(f"Area: {shape.area()}")
