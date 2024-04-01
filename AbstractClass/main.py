from abc import ABC, abstractmethod


class Shape(ABC):
    """
    A base abstract class representing a geometric shape.

    Methods:
        area: Abstract method to calculate the area of the shape.
    """
    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.

        This method must be implemented by subclasses.

        Raises:
            NotImplementedError: If the method is not implemented by subclasses.
        """


class Circle(Shape):
    """
    A class representing a circle, which is a type of shape.

    Attributes:
        radius (float): The radius of the circle.

    Methods:
        area: Calculate the area of the circle.
    """
    def __init__(self, radius):
        """
        Initialize a new instance of Circle.

        Parameters:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    """
    A class representing a rectangle, which is a type of shape.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Methods:
        area: Calculate the area of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initialize a new instance of Rectangle.

        Parameters:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height


circle = Circle(10)
rectangle = Rectangle(10, 5)

for shape in [circle, rectangle]:
    print(shape.area())
