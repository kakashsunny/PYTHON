# Object-Oriented Programming (OOP) in Python

## Definitions & Concepts
OOP is a programming paradigm based on the concept of "objects", which contain data (attributes) and code (methods).

## The Four Pillars of OOP
1. **Encapsulation**: Restricting direct access to some of the object's components. Private attributes are prefixed with double underscores `__`.
2. **Inheritance**: Creating new classes (child) from existing classes (parent).
3. **Polymorphism**: The ability to present the same interface for different underlying forms (e.g., different classes implementing the same method).
4. **Abstraction**: Hiding complex implementation details and showing only essential features (using abstract base classes).

## Syntax & Examples
```python
# Class Definition
class Animal:
    def __init__(self, name):
        self.name = name # Public attribute
        self.__id = 1234 # Private attribute (name mangled)

    def speak(self):
        pass

# Inheritance & Polymorphism
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Rex")
print(my_dog.speak())
```

## Best Practices
- Favor composition over inheritance where applicable.
- Follow the SOLID principles.
- Use `@classmethod` for alternative constructors and `@staticmethod` for utility functions associated with the class namespace.

## Common Mistakes
- Modifying class variables when intending to modify instance variables.
- Forgetting to call `super().__init__()` in the subclass constructor.

## Interview Tips
- **Q**: What is Name Mangling in Python?
- **A**: If a class attribute name starts with double underscores (e.g., `__private`), Python changes its name to `_ClassName__private` under the hood to prevent naming conflicts in subclasses.
