# 2D Shapes
import math

def square(side):
    """Gets the area of a square."""
    return side**2

def rectangle(length, width):
    """Gets the area of a rectangle."""
    return length * width

def triangle(base, height):
    """Gets the area of a triangle."""
    return 0.5 * base * height

def trapezoid(base1, base2, height):
    """Gets the area of a trapezoid."""
    return 0.5 * (base1 + base2) * height

def circle(radius):
    """Gets the area of a circle."""
    return math.pi * radius**2

def ellipse(major, minor):
    """Gets the area of an ellipse."""
    return math.pi * major * minor

# 3D shapes

def cube(side):
    """Gets the surface area of a cube."""
    return 6 * side**2

def cylinder(radius, height):
    """Gets the surface area of a cylinder."""
    return 2 * math.pi * radius * (radius + height)

def cone(radius, height):
    """Gets the surface area of a cone."""
    return math.pi * radius * (radius + math.hypot(height, radius))

def sphere(radius):
    """Gets the surface area of a sphere."""
    return 4 * math.pi * radius**2
