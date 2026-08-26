# Questions & Answers: Object-Oriented Programming

## MCQs
1. **Which built-in function checks if an object is an instance of a subclass?**
   - A) `type()`
   - B) `isinstance()`
   - C) `issubclass()`
   - D) `hasattr()`
   - **Answer**: B
   - **Explanation**: `isinstance(obj, Class)` checks if `obj` is an instance of `Class` or a subclass of it.

2. **What does the `@classmethod` decorator do?**
   - A) Converts a method into a static method.
   - B) Restricts instantiation.
   - C) Passes the class itself (`cls`) as the first argument instead of instance (`self`).
   - D) Private method indicator.
   - **Answer**: C
   - **Explanation**: Class methods operate on the class level rather than the instance level.

## Beginner & Intermediate Questions
### Q1: What is Method Resolution Order (MRO) in Python?
**Answer**: MRO is the order in which Python searches for inherited methods in multiple inheritance. Python uses the C3 Linearization algorithm to determine this order, which can be viewed using the `__mro__` attribute or `.mro()` method on a class.

### Q2: What is the difference between `__init__` and `__new__`?
**Answer**: `__new__` is the actual creator method that constructs and returns the new object instance, while `__init__` is the initializer method that initializes the attributes of the instance.

## Coding Practice & Solutions
### Problem: Create a class `Car` that keeps track of the total number of cars created.
**Solution**:
```python
class Car:
    total_cars = 0  # Class variable

    def __init__(self, model):
        self.model = model
        Car.total_cars += 1

c1 = Car("Tesla")
c2 = Car("Ford")
print(Car.total_cars)  # Output: 2
```
