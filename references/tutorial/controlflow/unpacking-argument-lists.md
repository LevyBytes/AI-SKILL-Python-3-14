# 4.9.5. Unpacking Argument Lists

### 4.9.5. Unpacking Argument Lists

The opposite scenario arises when your arguments already reside inside a list or tuple, yet a call demands them as distinct positional arguments. Take the built-in [`range()`](https://docs.python.org/3.14/library/stdtypes.html#range) function, which wants separate *start* and *stop* arguments. Should they not be at hand individually, code the call with the `*`-operator to spread the arguments out of a list or tuple:

```python
>>> list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]

```

Likewise, a dictionary can supply keyword arguments by way of the `**`-operator:

```python
>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !

```

[Subject index](INDEX.md) · [Previous source section](arbitrary-argument-lists.md) · [Following source section](lambda-expressions.md)
