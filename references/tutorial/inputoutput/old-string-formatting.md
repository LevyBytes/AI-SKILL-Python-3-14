# 7.1.4. Old string formatting

### 7.1.4. Old string formatting

String formatting is another job the % operator (modulo) can handle. With `format % values` (in which *format* is a string), the `%` conversion specifications inside *format* get swapped out for zero or more items drawn from *values*. People usually call this operation string interpolation. As an instance:

```python
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.

```

Additional details are available in the [printf-style String Formatting](https://docs.python.org/3.14/library/stdtypes.html#old-string-formatting) section.

[Subject index](INDEX.md) · [Previous source section](manual-string-formatting.md) · [Following source section](reading-and-writing-files.md)
