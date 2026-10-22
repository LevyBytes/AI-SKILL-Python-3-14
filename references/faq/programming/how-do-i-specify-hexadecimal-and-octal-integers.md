# How do I specify hexadecimal and octal integers?

### Numbers and strings

### How do I specify hexadecimal and octal integers?

To write an octal digit, put a zero ahead of the octal value, followed by a lower- or uppercase “o”. As an example, to assign the variable “a” the octal value “10” (which is 8 in decimal), enter:

```python
>>> a = 0o10
>>> a
8

```

Hexadecimal is equally straightforward. Just put a zero in front of the hexadecimal number, then a lower- or uppercase “x”. The hexadecimal digits themselves may be lower- or uppercase. For instance, within the Python interpreter:

```python
>>> a = 0xa5
>>> a
165
>>> b = 0XB2
>>> b
178

```

[Subject index](INDEX.md)
