# 4.9.4. Arbitrary Argument Lists

### 4.9.4. Arbitrary Argument Lists

The last and rarest choice is to declare that any number of arguments may be handed to a function. Those get bundled into a tuple (refer to [Tuples and Sequences](https://docs.python.org/3.14/tutorial/datastructures.html#tut-tuples)). Ahead of the variable-length portion, you may place zero or more ordinary arguments.

```python
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

```

Typically these *variadic* arguments sit at the tail of the formal parameter list, since they sweep up every leftover input argument handed to the function. Whatever formal parameters trail the `*args` parameter become ‘keyword-only’ arguments, so they may serve only as keywords and never as positional ones.

```python
>>> def concat(*args, sep="/"):
...     return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'

```

[Subject index](INDEX.md) · [Previous source section](recap.md) · [Following source section](unpacking-argument-lists.md)
