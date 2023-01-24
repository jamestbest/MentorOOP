# Inheritance example
class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


class Rectangle(Shape):
    def __init__(self, x, y, color, width, height):
        super().__init__(x, y, color)
        self.width = width
        self.height = height


class Circle(Shape):
    def __init__(self, x, y, color, radius):
        super().__init__(x, y, color)
        self.radius = radius


circle = Circle(10, 20, "red", 5)
rectangle = Rectangle(10, 20, "blue", 5, 10)


# Now let's say we want to remove the color attribute from the Shape class
# This will require changes to all subclasses (Rectangle and Circle) as we remove the color attribute as a parameter in the constructor
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius


circle = Circle(10, 20, 5)
rectangle = Rectangle(10, 20, 5, 10)


# Composition example
class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


class Rectangle:
    def __init__(self, shape, width, height):
        self.shape = shape
        self.width = width
        self.height = height


class Circle:
    def __init__(self, shape, radius):
        self.shape = shape
        self.radius = radius


circle = Circle(Shape(10, 20, "red"), 5)
rectangle = Rectangle(Shape(10, 20, "blue"), 5, 10)


# Now let's say we want to remove the color attribute from the Shape class
# This will only require changes to the Shape class and won't affect the other classes (Rectangle and Circle)
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, shape, width, height):
        self.shape = shape
        self.width = width
        self.height = height


class Circle:
    def __init__(self, shape, radius):
        self.shape = shape
        self.radius = radius


circle = Circle(Shape(10, 20), 5)
rectangle = Rectangle(Shape(10, 20), 5, 10)

# by using composition we only need to edit how we create the shape object and not the other classes

# composition also allows you to share the same shape object between multiple classes
# e.g. shape = Shape(10, 20)
#      circle = Circle(shape, 5)
#      rectangle = Rectangle(shape, 5, 10)

# in the inheritance example you would have to pass in the information for the shape object multiple times
# e.g. circle = Circle(10, 20, 5)
#      rectangle = Rectangle(10, 20, 5, 10)
