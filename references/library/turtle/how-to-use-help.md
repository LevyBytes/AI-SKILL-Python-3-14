# How to use help

### Help and configuration

### How to use help

Docstrings document the public methods of the Screen and Turtle classes in great detail. Therefore they double as online-help through Python’s help mechanisms:

- Within IDLE, tooltips reveal the signatures plus the opening lines of the docstrings for function-/method calls as you type them.

- Invoking [`help()`](https://docs.python.org/3.14/library/functions.html#help) on a method or function shows its docstrings:

```python
>>> help(Screen.bgcolor)
Help on method bgcolor in module turtle:

bgcolor(self, *args) unbound turtle.Screen method
    Set or return backgroundcolor of the TurtleScreen.

    Arguments (if given): a color string or three numbers
    in the range 0..colormode or a 3-tuple of such numbers.

    >>> screen.bgcolor("orange")
    >>> screen.bgcolor()
    "orange"
    >>> screen.bgcolor(0.5,0,0.5)
    >>> screen.bgcolor()
    "#800080"

>>> help(Turtle.penup)
Help on method penup in module turtle:

penup(self) unbound turtle.Turtle method
    Pull the pen up -- no drawing when moving.

    Aliases: penup | pu | up

    No argument

    >>> turtle.penup()

```

- The functions that are derived from methods carry docstrings in an altered form:

```python
>>> help(bgcolor)
Help on function bgcolor in module turtle:

bgcolor(*args)
    Set or return backgroundcolor of the TurtleScreen.

    Arguments (if given): a color string or three numbers
    in the range 0..colormode or a 3-tuple of such numbers.

    Example::

      >>> bgcolor("orange")
      >>> bgcolor()
      "orange"
      >>> bgcolor(0.5,0,0.5)
      >>> bgcolor()
      "#800080"

>>> help(penup)
Help on function penup in module turtle:

penup()
    Pull the pen up -- no drawing when moving.

    Aliases: penup | pu | up

    No argument

    Example:
    >>> penup()

```

These altered docstrings get produced automatically alongside the function definitions that are derived from the methods at import time.

[Subject index](INDEX.md) · [Continue](turtle-write-docstringdict.md)
