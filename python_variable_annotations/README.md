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
- Task 2:  Write a type-annotated function floor which takes a float n as argument and returns the floor of the float.
- Task 3:  Write a type-annotated function to_str that takes a float n as argument and returns the string representation of the float.
- Task 4:  Define and annotate the following variables with the specified values:
    - a, an integer with a value of 1
    - pi, a float with a value of 3.14
    - i_understand_annotations, a boolean with a value of True
    - school, a string with a value of “Holberton"
- Task 5:  Write a type-annotated function sum_list which takes a list input_list of floats as argument and returns their sum as a float.