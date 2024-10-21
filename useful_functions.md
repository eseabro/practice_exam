## Random
```python
import random
random.seed(a=None, version=2) # To initialize a random seed
random.randrange(start, stop[, step]) # Return a randomly selected element from range(start, stop, step).
random.randint(a, b) # Random number between a and b inclusive
random.choice(seq) # Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.
random.shuffle(x) # Shuffle sequence x in place. returns None
```

## Useful numpy functions
```python
import numpy as np

# Basic
a = np.array([1,2,3])
a = np.ones((2,4))
a = np.zeros((3,3))
a = np.arange(start, stop, delta)
a = np.linspace(start, stop, N)
a = np.random.random((3, 3))  # 3x3 array of random numbers
a = np.random.randint(1, 10, (2, 2))  # 2x2 matrix of random integers between 1 and 9

# Operations
b = np.add([1, 2], [3, 4])  # [4, 6]
b = np.subtract([5, 6], [3, 2])  # [2, 4]
b = np.multiply([1, 2], [3, 4])  # [3, 8]
b = np.divide([6, 8], [2, 4])  # [3.0, 2.0]
b = np.dot([1, 2], [3, 4])  # 1*3 + 2*4 = 11
b = np.sum([1, 2, 3])  # 6
b = np.mean([1, 2, 3, 4])  # 2.5
b = np.max([1, 2, 3])  # 3
b = np.min([1, 2, 3])  # 1
b = np.std([1, 2, 3, 4])  # 1.118033988749895

# Reshaping
arr = np.array([1, 2, 3, 4])
c = arr.reshape((2, 2))  # 2x2 matrix [[1, 2], [3, 4]]

c = np.transpose([[1, 2], [3, 4]])  # [[1, 3], [2, 4]]
c = np.array([[1, 2], [3, 4]]).flatten()  # [1, 2, 3, 4]
c = np.vstack(([1, 2], [3, 4]))  # [[1, 2], [3, 4]]
c = np.hstack(([1, 2], [3, 4]))  # [1, 2, 3, 4]

# Array indexing and slicing
d = np.where([1, 2, 3, 4] > 2)  # (array([2, 3]),)

arr = np.array([10, 20, 30, 40])
d = np.take(arr, [0, 2])  # [10, 30]

d = np.argmax([1, 3, 2])  # 1 (index of the largest value, 3)
d = np.argmin([1, 3, 2])  # 0 (index of the smallest value, 1)

# Lin alg
e = np.linalg.inv([[1, 2], [3, 4]])
e = np.linalg.det([[1, 2], [3, 4]])  # -2.0
e = np.linalg.eig([[1, 2], [3, 4]])

A = np.array([[3, 1], [1, 2]])
B = np.array([9, 8])
e = np.linalg.solve(A, B)  # [2. 3.]

# Random
f = np.random.choice([1, 2, 3, 4], size=2)  # Random 2 elements
f = np.random.normal(0, 1, size=(2, 3))  # 2x3 array from normal distribution

```

## Functions

### Function Definition
```python
def function_name(parameters):
    """Optional docstring describing the function."""
    # Function body
    return value  # Optional return statement

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def my_function(*args, **kwargs):
    """Handles variable numbers of arguments."""
    print(args)      # Tuple of positional arguments
    print(kwargs)    # Dictionary of keyword arguments

def calculate(a, b):
    return a + b, a - b, a * b, a / b       # Returns multiple arguments as a tuple!

# inline
square = lambda x: x ** 2

```

## Classes
```python
class ClassName:
    """Optional docstring describing the class."""
    
    def __init__(self, parameters):
        """Constructor method to initialize attributes."""
        self.attribute = value  # Instance attributes

    def method(self):
        """A method of the class."""
        # Method body
```

### Inheritance

```python
class ParentClass:
    """Parent class."""
    
class ChildClass(ParentClass):
    """Child class that inherits from ParentClass."""
```

### Static methods
These won't require class instances to run

```python
class MyClass:
    @staticmethod
    def static_method():
        return "This is a static method."
```

## List operations
*Remember that list operations are inplace*

```python
my_list = []

my_list.append(1)
my_list.extend(1)
my_list.insert(1)
my_list.remove(1)
my_list.pop(1)
my_list.sort(1)
my_list.reverse(1)
newlist = my_list.copy()
```

## Loops
Break and Continue:
   - *break* to exit a loop
   - *continue* to skip to the next iteration

## File Handling

### Reading
**Reading Modes**: 'r': read, 'w':write, 'a':append, 'a+': append to file and create if it doesn't exist
```python
with open('file.txt', 'r') as file:
    content = file.read()
```

### Writing
```python
with open('file.txt', 'w') as file:
    file.write("Hello, World!")
```

### Try - except
```python
try:
    # code that may cause an exception
except ExceptionType:
    # code to handle the exception
```

## Useful built-in functions:
```python
len(), type(), str(), int(), float(), list(), dict(), set()
map(), filter(), reduce()
any(), all(), sum()
count(), index() # List
keys(), values(), items() # Dictionary
```

## `enumerate` Cheat Sheet

The `enumerate` function adds a counter to an iterable (like a list) and returns it as an `enumerate` object. This is particularly useful for getting both the index and the value of items in a loop.

### Syntax

```python
enumerate(iterable, start=0)
```
*iterable:* The collection you want to enumerate (e.g., a list, tuple, string).
*start (optional):* The starting index (default is 0).

### Basic example:
```python
my_list = ['apple', 'banana', 'cherry']

for index, value in enumerate(my_list):
    print(index, value)
```

### With list comprehension

```python
my_list = ['apple', 'banana', 'cherry']
indexed_list = [(index, value) for index, value in enumerate(my_list)]
print(indexed_list)
```

## Matplotlib Cheat Sheet

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.

### Line plot
```python
plt.plot(x, y, label='Line', color='b', linestyle='-', marker='o')
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()
```

### Scatter Plot
```python
plt.scatter(x, y, color='r', marker='x')
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
```

### Bar plot
```python
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 2, 5]

plt.bar(categories, values, color='g')
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
```

### Histogram
```python
data = [1, 2, 1, 2, 3, 4, 3, 4, 3, 2, 1, 2]
plt.hist(data, bins=4, color='purple', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
```

### Pie chart
```python
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()
```

### Modifiers:
```python
plt.grid(True)  # Turn on the grid
plt.figure(figsize=(10, 5))  # Width, Height in inches
plt.savefig('plot.png')  # Save the current figure

```

### Subplots:
```python
fig, axs = plt.subplots(2, 2)  # 2 rows, 2 columns
axs[0, 0].plot(x, y)
axs[0, 1].scatter(x, y)
axs[1, 0].bar(categories, values)
axs[1, 1].hist(data)
plt.tight_layout()  # Adjust spacing
plt.show()
```


### Line Styles

- **Solid Line**: `'-'` or `None`
- **Dashed Line**: `'--'`
- **Dash-dot Line**: `'-.'`
- **Dotted Line**: `':'`

### Colors
Matplotlib supports multiple ways to specify colors:

**Named Colors:** 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'
**Shortened:** 'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'

**Hexadecimal Colors:**
    Use #RRGGBB format.
    Example: '#FF5733' (orange-red).

**RGB and RGBA Tuple:**
    RGB: (R, G, B) values in [0, 1].
    RGBA: (R, G, B, A) where A is alpha (transparency).
    Example: (0.1, 0.2, 0.5) for RGB or (0.1, 0.2, 0.5, 0.7) for RGBA.


## Getting help with unknown functions

Get help for any function (example with np.arange but works with any):
Type python into the terminal after activating your conda environment.

```py
    > python
    >>> import numpy as np
    >>> help(np.arange)
```