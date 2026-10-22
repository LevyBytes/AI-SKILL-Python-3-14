# What’s New in Python 2.7 / PEP 3137: The memoryview Object

### PEP 3137: The memoryview Object

A [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) gives you a window onto the memory backing some other object, and it presents that data through the same interface the [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) type uses.

```pycon
>>> import string
>>> m = memoryview(string.letters)
>>> m
<memory at 0x37f850>
>>> len(m)           # Returns length of underlying object
52
>>> m[0], m[25], m[26]   # Indexing returns one byte
('a', 'z', 'A')
>>> m2 = m[0:26]         # Slicing returns another memoryview
>>> m2
<memory at 0x37f080>

```

What the view holds can be turned into either a byte string or a list of integers:

```pycon
>>> m2.tobytes()
'abcdefghijklmnopqrstuvwxyz'
>>> m2.tolist()
[97, 98, 99, 100, 101, 102, 103, ... 121, 122]
>>>

```

Should the backing object happen to be mutable, a [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) lets you change it.

```pycon
>>> m2[0] = 75
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot modify read-only memory
>>> b = bytearray(string.letters)  # Creating a mutable object
>>> b
bytearray(b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
>>> mb = memoryview(b)
>>> mb[0] = '*'         # Assign to view, changing the bytearray.
>>> b[0:5]              # The bytearray has been changed.
bytearray(b'*bcde')
>>>

```

See also

[**PEP 3137**](https://peps.python.org/pep-3137/) - Immutable Bytes and Mutable Buffer

Guido van Rossum drafted the PEP; the implementation came from Travis Oliphant, Antoine Pitrou and others, and the back-port to 2.7 was carried out by Antoine Pitrou, recorded as [bpo-2396](https://bugs.python.org/issue?@action=redirect&bpo=2396).

[Subject index](INDEX.md) · [Previous source section](pep-3106-dictionary-views.md) · [Next source section](core-language-changes.md) · [Release/subject declaration](the-future-for-python-2-x.md)
