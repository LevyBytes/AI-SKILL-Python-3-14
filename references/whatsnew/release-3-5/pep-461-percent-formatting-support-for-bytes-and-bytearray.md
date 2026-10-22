# What’s New In Python 3.5 / PEP 461 - percent formatting support for bytes and bytearray

### PEP 461 - percent formatting support for bytes and bytearray

[**PEP 461**](https://peps.python.org/pep-0461/) brings the `%` [interpolation operator](https://docs.python.org/3.14/library/stdtypes.html#bytes-formatting) to [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray).

Interpolation is most often pictured as a string-side operation, yet there are scenarios in which interpolating across `bytes` or `bytearrays` is reasonable, and the extra effort required to compensate for that gap hurts how readable the code stays. The matter becomes especially relevant when handling wire format protocols, which frequently blend binary data with ASCII compatible text.

Examples:

```python
>>> b'Hello %b!' % b'World'
b'Hello World!'

>>> b'x=%i y=%f' % (1, 2.5)
b'x=1 y=2.500000'

```

Unicode is not allowed for `%b`, but it is accepted by `%a` (equivalent of `repr(obj).encode('ascii', 'backslashreplace')`):

```python
>>> b'Hello %b!' % 'World'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: %b requires bytes, or an object that implements __bytes__, not 'str'

>>> b'price: %a' % '10€'
b"price: '10\\u20ac'"

```

Keep in mind that the `%s` and `%r` conversion types, while permitted, ought to appear only where a codebase still has to stay compatible with Python 2.

See also

[**PEP 461**](https://peps.python.org/pep-0461/) – Adding % formatting to bytes and bytearray

PEP written by Ethan Furman; implemented by Neil Schemenauer and Ethan Furman.

[Subject index](INDEX.md) · [Previous source section](pep-448-additional-unpacking-generalizations.md) · [Next source section](pep-484-type-hints.md) · [Release/subject declaration](summary-release-highlights.md)
