"""Module providing a solution to Problem Set 00.

Write a program that does the following in order:

1. At the top of your file and type: import numpy
2. Now write a line that sets a variable named `x` to 5.
3. Now write a line that sets a variable named `y` to 8.
4. Add variables x and y, and save the result to a variable named `z`.
5. Now save the result of this command: numpy.log2(z) to a variable named `a`.
"""

import numpy


if __name__ == "__main__":
    x = 5
    y = 8
    z = x + y
    a = numpy.log2(z)
    print(a)
