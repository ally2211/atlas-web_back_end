## Python - Variable Annotations
## General

- **Type annotations in Python 3**  
 ```python
 def add(x: int, y: int) -> int:
    return x + y
```
- **How you can use type annotations to specify function signatures and variable types**
- **Duck typing**
has the necessary methods or properties
```python
def quack(duck):
    duck.quack()
    duck.fly()
```
- **How to validate your code with `mypy`**
``` python
pip install mypy
mypy your_script.py
```

### Tasks:
- Task 0:  Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.
- Task 1:  Write a type-annotated function concat that takes a string str1 and a string str2 as arguments and returns a concatenated string