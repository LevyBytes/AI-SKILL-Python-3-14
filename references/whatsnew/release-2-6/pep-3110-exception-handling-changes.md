# What’s New in Python 2.6 / PEP 3110: Exception-Handling Changes

### PEP 3110: Exception-Handling Changes

A mistake Python programmers sometimes commit is to write code shaped like this:

```python
try:
    ...
except TypeError, ValueError:  # Wrong!
    ...

```

What the author most likely intends is to trap both [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) and [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), yet the code behaves otherwise: it traps `TypeError` and assigns the caught exception object to the local name `"ValueError"`. As a result the `ValueError` exception goes entirely uncaught. The proper form names a tuple of exceptions:

```python
try:
    ...
except (TypeError, ValueError):
    ...

```

The root of the mistake is the comma's ambiguity: is it marking two separate nodes in the parse tree, or one node that happens to be a tuple?

Python 3.0 settles the ambiguity by swapping the comma for the keyword "as". So that you can trap an exception and keep the exception object inside the variable `exc`, the spelling becomes:

```python
try:
    ...
except TypeError as exc:
    ...

```

Because Python 3.0 accepts only the "as" spelling, it reads the earlier example as catching two distinct exceptions. Python 2.6 honors both the comma form and "as", so code already written keeps functioning. Hence we recommend reaching for "as" in fresh Python code meant to run solely under 2.6.

See also

[**PEP 3110**](https://peps.python.org/pep-3110/) - Catching Exceptions in Python 3000

PEP written and implemented by Collin Winter.

[Subject index](INDEX.md) · [Previous source section](pep-3105-print-as-a-function.md) · [Next source section](pep-3112-byte-literals.md) · [Release/subject declaration](python-3-0.md)
