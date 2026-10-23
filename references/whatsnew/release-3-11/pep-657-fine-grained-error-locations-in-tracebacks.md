# What's New In Python 3.11 / PEP 657: Fine-grained error locations in tracebacks - dis

### New Features

### PEP 657: Fine-grained error locations in tracebacks

While rendering a traceback, the runtime now highlights the precise subexpression responsible for the failure rather than the whole line. Take this case:

```python
Traceback (most recent call last):
  File "distance.py", line 11, in <module>
    print(manhattan_distance(p1, p2))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "distance.py", line 6, in manhattan_distance
    return abs(point_1.x - point_2.x) + abs(point_1.y - point_2.y)
                           ^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'x'

```

Earlier releases highlighted only the line, which left it unclear which value happened to be `None`. The richer diagnostics also pay off across deeply nested [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) objects together with chained function calls:

```python
Traceback (most recent call last):
  File "query.py", line 37, in <module>
    magic_arithmetic('foo')
  File "query.py", line 18, in magic_arithmetic
    return add_counts(x) / 25
           ^^^^^^^^^^^^^
  File "query.py", line 24, in add_counts
    return 25 + query_user(user1) + query_user(user2)
                ^^^^^^^^^^^^^^^^^
  File "query.py", line 32, in query_user
    return 1 + query_count(db, response['a']['b']['c']['user'], retry=True)
                               ~~~~~~~~~~~~~~~~~~^^^^^
TypeError: 'NoneType' object is not subscriptable

```

And likewise for involved arithmetic:

```python
Traceback (most recent call last):
  File "calculation.py", line 54, in <module>
    result = (x / y / z) * (a / b / c)
              ~~~~~~^~~
ZeroDivisionError: division by zero

```

Beyond that, the data driving these richer tracebacks is exposed through a general-purpose API, letting you map [bytecode](https://docs.python.org/3.14/glossary.html#term-bytecode) [instructions](https://docs.python.org/3.14/library/dis.html#bytecodes) back to where they sit in source. Two routes give you that data:

- The [`codeobject.co_positions()`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_positions) method in Python.

- The [`PyCode_Addr2Location()`](https://docs.python.org/3.14/c-api/code.html#c.PyCode_Addr2Location) function in the C API.

Consult [**PEP 657**](https://peps.python.org/pep-0657/) for the full treatment.
> (Contributed by Pablo Galindo, Batuhan Taskaya and Ammar Askar in [bpo-43950](https://bugs.python.org/issue?@action=redirect&bpo=43950).)

Note

Because this capability keeps column offsets inside [Code Objects](https://docs.python.org/3.14/c-api/code.html#codeobjects), compiled Python files may grow slightly and the interpreter may use a touch more memory. If you would rather skip recording that data and suppress the extra traceback detail, reach for the [`-X no_debug_ranges`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command line option or the [`PYTHONNODEBUGRANGES`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONNODEBUGRANGES) environment variable.

[Subject index](INDEX.md) · [Previous source section](summary-release-highlights.md) · [Next source section](pep-654-exception-groups-and-except.md) · [Release/subject declaration](summary-release-highlights.md)
