# What’s New In Python 3.5 / PEP 465 - A dedicated infix operator for matrix multiplication

### PEP 465 - A dedicated infix operator for matrix multiplication

[**PEP 465**](https://peps.python.org/pep-0465/) supplies the `@` infix operator dedicated to matrix multiplication. At present none of the builtin Python types provide the operator, yet you can wire it up by defining [`__matmul__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__matmul__), [`__rmatmul__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__rmatmul__), and [`__imatmul__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__imatmul__) to cover regular, reflected, and in-place matrix multiplication. How these methods behave parallels the methods that supply the other infix arithmetic operators.

Across many areas of mathematics, science, and engineering, matrix multiplication shows up especially often, and bringing in `@` lets you express tidier code:

```python
S = (H @ beta - r).T @ inv(H @ V @ H.T) @ (H @ beta - r)

```

instead of:

```python
S = dot((dot(H, beta) - r).T,
        dot(inv(dot(dot(H, V), H.T)), dot(H, beta) - r))

```

NumPy 1.10 has support for the new operator:

```python
>>> import numpy

>>> x = numpy.ones(3)
>>> x
array([ 1., 1., 1.])

>>> m = numpy.eye(3)
>>> m
array([[ 1., 0., 0.],
       [ 0., 1., 0.],
       [ 0., 0., 1.]])

>>> x @ m
array([ 1., 1., 1.])

```

See also

[**PEP 465**](https://peps.python.org/pep-0465/) – A dedicated infix operator for matrix multiplication

PEP written by Nathaniel J. Smith; implemented by Benjamin Peterson.

[Subject index](INDEX.md) · [Previous source section](pep-492-coroutines-with-async-and-await-syntax-note.md) · [Next source section](pep-448-additional-unpacking-generalizations.md) · [Release/subject declaration](summary-release-highlights.md)
