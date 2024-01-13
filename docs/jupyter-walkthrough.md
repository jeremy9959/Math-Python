---
layout: default
title: Jupyter Walkthrough
nav_order: 2
---

# Jupyter Lab Project Walkthrough

1. Use the 'text editor' feature in Jupyter Lab to create your README.md file.
2. **RENAME YOUR NOTEBOOK FILE IMMEDIATELY** to something relevant
3. CTRL-ENTER executes a cell.

## Markdown cells

This is a markdown cell:

- Headings are \#, \#\#, etc.
- Bold is marked \*\*make me bold\*\* like **this**.
- Italics are marked \*make me italic\* like *this*.
- Math can be typeset with \LaTeX if you know it:  $$f(x)=e^{-x}\cos(x)$$
- Bulleted lists are marked with \-.

```{python}
# | tags: []
# code cells
## Code cells contain python code that gets executed.
# indicates a comment that is ignored.
print("Hello World!")
```

In this walkthrough we will look at the following elements of Python in a jupyter notebook.

The print statement

```{python}
print("hello world!")
```


Variables, variable names, and assignment/datatypes

```{python}
count = 5  # an integer
name = "Jeremy Teitelbaum"  # a string
paragraph = """This is how you enter a multiline string
in python. It is enclosed in triple quotes."""
pi = 3.14159  # a float
epsilon = 1.0e-6  # a float
students = ["Jeremy", "Phillip", "Sara", "Molly"]  # a list
HotDog = True

```

```{python}
print(students)
```

Compare `print` for multiline strings with the string value. (\\n means newline)


```{python}
print(paragraph)
```

```{python}
paragraph
```

Arithmetic operations

```{python}
print(count)
count = count + 1
print(count)
```

```{python}
1 / pi
```

```{python}
print(2**3)  # exponent
print(1 / 2)  # division (converts integer to float)
print(1 / (1 / 2))  # 2 becomes 2.0
```

```{python}
quotient = 5 // 3  # integer division
remainder = 5 % 3  # remainder
print(quotient, remainder)
```


Operations on strings and lists

```{python}
"Jeremy" + " Teitelbaum"
```

```{python}
["a", "b", "c"] + ["d"]
```

```{python}
len("Jeremy")
```

```{python}
len(["Jeremy", "Teitelbaum"])
```

```{python}
firstName = "Jeremy"
lastName = "Teitelbaum"
fullName = firstName + " " + lastName
```

Some fancier printing

```{python}
print(f"The first name is {firstName}")
print(f"The last name is {lastName}")
print(f"The full name is {firstName} {lastName}")
print(firstName, lastName, sep=",")
print(firstName, lastName, sep=":")
```

Slicing

In python, we **always count from zero**!!!

```{python}
firstName[0]
```

```{python}
lastName[1]
```

```{python}
# [a:b] means from a to b-1 inclusive

print(firstName[0:3])
print(firstName[3:])
print(firstName[3:5])
```

```{python}
# negative indices count from the end
print(firstName[-1])  # the last element
print(firstName[-3:-1])  # elements -3 and -2, but not -1
```

```{python}
# [a:b:c] means from a to b-1 in steps of c
# missing numbers mean (beginnging):(end)
print(firstName[:5:2])
print(firstName[::2])
print(firstName[::-1])  # reverse the string
print(firstName[3::-1])  # 3,2,1,0
print(firstName[3:0:-1])  # 3,2,1
```

Slices work the same on list elements

```{python}
print(students[0])
print(students[-1])
every_other_student = students[::2]
print(every_other_student)
```

Libraries

```{python}
import math

```

```{python}
math.log(23)
```

```{python}
math.pi
```

```{python}
math.cos(math.pi / 2)  # should be zero
```

```{python}
math.cos(math.pi / 2) == 0
```

```{python}
abs(math.cos(math.pi / 2)) < 1e-6
```

```{python}
math.pi == pi
```

```{python}
import numpy as np

```


```{python}
print(np.random.randint(0, 10))
```

```{python}
print(np.__version__)
```

```{python}
from numpy.random import randint

```

```{python}
randint(1, 10)
```

## Numpy arrays

A numpy array is like a list, but:

    - it's itended for use with numbers
    - it's designed for fast arithmetic and numerical operations
    - it can be multi-dimensional -- like a table or matrix -- although we won't use that here.


```{python}
x = np.array([1, 2, 3, 4, 5, 6])
print(x)
```

You access arrays like lists, and can use slices; indices start at zero.

```{python}
x[2:4]
```

When you apply an operation to an array, it gets applied to every element of the array.

```{python}
print(f"Square of x is {x**2}")
print(f"1/x is {1/x}")
print(f"cos(x) is {np.cos(x)}")
```

Some special arrays.

```{python}
x = np.zeros(10)  # 10 zeros
y = np.ones(20)  # 20 ones
z = np.linspace(0, 10, 100)  # 100 equally spaced numbers from 0 to 10 **inclusive**
w = np.array(list(range(-10, 10, 2)))
```

```{python}
print(w)
```

```{python}
print(z)
```

```{python}
## Plotting with matplotlib
```

```{python}
import matplotlib.pyplot as plt

```

```{python}
plt.plot(z, z**2)
```

```{python}
z = np.linspace(-10, 10, 100)
plt.axes()
plt.plot(z, np.cos(z), color="red")
plt.title("A cosine curve")
plt.grid()
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.xticks(list(range(-10, 11)))
plt.xlabel("x")
plt.ylabel("y")
```


