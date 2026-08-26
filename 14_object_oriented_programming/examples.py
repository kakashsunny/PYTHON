# Object-Oriented Programming Examples and Practice
from abc import ABC, abstractmethod

# 1. Abstraction (Abstract Base Class)
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# 2. Inheritance and Polymorphism
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Using Polymorphism
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"Area of {type(shape).__name__}: {shape.area():.2f}")

# 3. Encapsulation & Property Decorator
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # Private

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            raise ValueError("Balance cannot be negative.")

acc = Account("Bob", 1000)
print("Balance:", acc.balance)
acc.balance = 1200
print("New Balance:", acc.balance)
