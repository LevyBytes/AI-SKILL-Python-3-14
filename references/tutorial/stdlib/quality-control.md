# 10.11. Quality control

### 10.11. Quality control

A solid path toward dependable software is to author a test for every function right as you build it, then exercise those tests often throughout development.

With the [`doctest`](https://docs.python.org/3.14/library/doctest.html#module-doctest) module you can sweep through a module and confirm the tests tucked inside a program's docstrings. Writing such a test takes no more than pasting a representative call together with its output into the docstring. That enriches the docs by handing the reader a worked example, while letting the doctest module verify the code still matches what the documentation claims:

```python
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests

```

Though the [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) module takes more effort than [`doctest`](https://docs.python.org/3.14/library/doctest.html#module-doctest), it lets you keep a richer suite of tests in a file of their own:

```python
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests

```

[Subject index](INDEX.md) · [Previous source section](performance-measurement.md) · [Following source section](batteries-included.md)
