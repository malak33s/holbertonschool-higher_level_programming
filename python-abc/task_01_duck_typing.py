#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math

# Shape Abstract Class
class Shape(ABC):
    """Abstract class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass

# Circle Class
class Circle(Shape):
    """Circle class inheriting from Shape."""
    
    def __init__(self, radius):
        """Initialize the circle with its radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter of the circle (circumference)."""
        return 2 * math.pi * self.radius

# Rectangle Class
class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""
    
    def __init__(self, width, height):
        """Initialize the rectangle with its width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""