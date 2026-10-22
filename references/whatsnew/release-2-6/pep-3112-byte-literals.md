# What’s New in Python 2.6 / PEP 3112: Byte Literals

### PEP 3112: Byte Literals

Python 3.0 makes Unicode the language's core string type and writes 8-bit literals in a separate fashion, spelling them either as `b'string'` or via a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) constructor. So that future code ports cleanly, Python 2.6 introduces `bytes` as an alias for the [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) type and likewise accepts the `b''` spelling.

The 2.6 [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) parts ways with the 3.0 [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) type on several fronts; the constructor especially behaves nothing alike. Under 3.0, `bytes([65, 66, 67])` has 3 elements and holds the bytes that spell `ABC`; under 2.6, `bytes([65, 66, 67])` hands back the 12-byte string giving the [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) of that list.

In 2.6 the main reason to reach for [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) is to author type checks such as `isinstance(x, bytes)`. That assists the 2to3 converter, which has no way to know whether 2.x code means its strings to carry characters or 8-bit bytes; you may now signal your meaning precisely with either `bytes` or [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), and the resulting code stays correct under Python 3.0 too.

A `__future__` import is likewise available that promotes every string literal to a Unicode string. As a consequence `\u` escape sequences become usable for embedding Unicode characters:

```python
from __future__ import unicode_literals

s = ('\u751f\u3080\u304e\u3000\u751f\u3054'
     '\u3081\u3000\u751f\u305f\u307e\u3054')

print len(s)               # 12 Unicode characters

```

Down at the C layer, Python 3.0 renames the older 8-bit string type, known as `PyStringObject` in Python 2.x, into [`PyBytesObject`](https://docs.python.org/3.14/c-api/bytes.html#c.PyBytesObject). Python 2.6 leans on `#define` so that the names [`PyBytesObject()`](https://docs.python.org/3.14/c-api/bytes.html#c.PyBytesObject), [`PyBytes_Check()`](https://docs.python.org/3.14/c-api/bytes.html#c.PyBytes_Check), [`PyBytes_FromStringAndSize()`](https://docs.python.org/3.14/c-api/bytes.html#c.PyBytes_FromStringAndSize), along with every other string-related function and macro, become usable.

Like strings, instances of the [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) type cannot be changed. A fresh [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) type, by contrast, keeps a mutable sequence of bytes:

```python
>>> bytearray([65, 66, 67])
bytearray(b'ABC')
>>> b = bytearray(u'\u21ef\u3244', 'utf-8')
>>> b
bytearray(b'\xe2\x87\xaf\xe3\x89\x84')
>>> b[0] = '\xe3'
>>> b
bytearray(b'\xe3\x87\xaf\xe3\x89\x84')
>>> unicode(str(b), 'utf-8')
u'\u31ef \u3244'

```

Byte arrays carry most string-type methods, among them [`startswith()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.startswith)/[`endswith()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.endswith), [`find()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.find)/[`rfind()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.rfind), plus several list methods like [`append()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.append), [`pop()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.pop), and [`reverse()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.reverse).

```python
>>> b = bytearray('ABC')
>>> b.append('d')
>>> b.append(ord('e'))
>>> b
bytearray(b'ABCde')

```

A matching C API accompanies it as well, featuring [`PyByteArray_FromObject()`](https://docs.python.org/3.14/c-api/bytearray.html#c.PyByteArray_FromObject), [`PyByteArray_FromStringAndSize()`](https://docs.python.org/3.14/c-api/bytearray.html#c.PyByteArray_FromStringAndSize), and assorted further functions.

See also

[**PEP 3112**](https://peps.python.org/pep-3112/) - Bytes literals in Python 3000

PEP written by Jason Orendorff; backported to 2.6 by Christian Heimes.

[Subject index](INDEX.md) · [Previous source section](pep-3110-exception-handling-changes.md) · [Next source section](pep-3116-new-i-o-library.md) · [Release/subject declaration](python-3-0.md)
