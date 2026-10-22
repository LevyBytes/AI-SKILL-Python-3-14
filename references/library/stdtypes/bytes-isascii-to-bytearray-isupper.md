# stdtypes: Bytes and bytearray ASCII character classification

bytes.isascii()

 bytearray.isascii()

Yield `True` when the sequence is empty or every byte in the sequence is ASCII; otherwise yield `False`. ASCII bytes sit in the range 0-0x7F.

Added in version 3.7.

 bytes.isdigit()

 bytearray.isdigit()

Yield `True` when every byte in the sequence is an ASCII decimal digit and the sequence is non-empty; otherwise yield `False`. ASCII decimal digits are the byte values in the sequence `b'0123456789'`.

As an illustration:

```python
>>> b'1234'.isdigit()
True
>>> b'1.23'.isdigit()
False

```

 bytes.islower()

 bytearray.islower()

Yield `True` when the sequence holds at least one lowercase ASCII character and no uppercase ASCII characters; otherwise yield `False`.

As an illustration:

```python
>>> b'hello world'.islower()
True
>>> b'Hello world'.islower()
False

```

Lowercase ASCII characters are the byte values in the sequence `b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters are the byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

 bytes.isspace()

 bytearray.isspace()

Yield `True` when every byte in the sequence is ASCII whitespace and the sequence is non-empty; otherwise yield `False`. The ASCII whitespace characters comprise the byte values within `b' \t\n\r\x0b\f'`, namely the space, the tab, the newline, the carriage return, plus the vertical tab and the form feed.

 bytes.istitle()

 bytearray.istitle()

Yield `True` when the sequence is ASCII titlecase and the sequence is non-empty; otherwise yield `False`. Consult `bytes.title()` for fuller detail on how "titlecase" is defined.

As an illustration:

```python
>>> b'Hello World'.istitle()
True
>>> b'Hello world'.istitle()
False

```

 bytes.isupper()

 bytearray.isupper()

Yield `True` when the sequence holds at least one uppercase alphabetic ASCII character and no lowercase ASCII characters; otherwise yield `False`.

As an illustration:

```python
>>> b'HELLO WORLD'.isupper()
True
>>> b'Hello world'.isupper()
False

```

Lowercase ASCII characters are the byte values in the sequence `b'abcdefghijklmnopqrstuvwxyz'`. Uppercase ASCII characters are the byte values in the sequence `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`.

[Subject index](INDEX.md) · [Previous](bytes-strip-to-bytearray-isalpha.md) · [Continue](bytes-lower-to-bytearray-swapcase.md) · [Owning module, declaration or section: Bytes and Bytearray Operations](bytes-count-to-bytearray-removeprefix.md)
