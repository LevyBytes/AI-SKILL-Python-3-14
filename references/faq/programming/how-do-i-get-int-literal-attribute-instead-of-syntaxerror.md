# How do I get int literal attribute instead of SyntaxError?

### How do I get int literal attribute instead of SyntaxError?

Attempting to access an `int` literal attribute the usual way yields a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError), since the period gets read as a decimal point:

```python
>>> 1.__class__
  File "<stdin>", line 1
  1.__class__
   ^
SyntaxError: invalid decimal literal

```

The fix is to put either a space or parentheses between the literal and the period.

```python
>>> 1 .__class__
<class 'int'>
>>> (1).__class__
<class 'int'>

```

[Subject index](INDEX.md)
