import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        if scalar != 0:
            return Vector(self.x / scalar, self.y / scalar)
        else:
            raise ValueError("Cannot divide by zero")

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        magnitude = self.magnitude()
        if magnitude != 0:
            return self / magnitude
        else:
            return Vector(0, 0)

    def perpendicular(self):
        return Vector(-self.y, self.x)

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def angle_with(self, other):
        dot_product = self.dot(other)
        magnitudes = self.magnitude() * other.magnitude()
        if magnitudes == 0:
            raise ValueError("Cannot calculate angle with zero-length vector")
        return math.acos(dot_product / magnitudes)

    def limit(self, max_magnitude):
        magnitude = self.magnitude()
        if magnitude > max_magnitude:
            return self.normalize() * max_magnitude
        return self
