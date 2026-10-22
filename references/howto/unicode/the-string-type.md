# The String Type

### The String Type

Beginning with Python 3.0, the [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) type holds Unicode characters, so any string built with `"unicode rocks!"`, `'unicode rocks!'`, or the triple-quoted string syntax is kept as Unicode.

Since UTF-8 is the default encoding for Python source code, you can drop a Unicode character straight into a string literal:

```python
try:
    with open('/tmp/input.txt', 'r') as f:
        ...
except OSError:
    # 'File not found' error message.
    print("Fichier non trouvé")

```

As an aside: Python 3 permits Unicode characters within identifiers as well:

```python
répertoire = "/tmp/records.log"
with open(répertoire, "w") as f:
    f.write("test\n")

```

When a given character can’t be typed in your editor, or when you wish to keep the source code ASCII-only for whatever reason, escape sequences can be used in string literals too. (Your system may show the actual capital-delta glyph rather than a u escape.)

```python
>>> "\N{GREEK CAPITAL LETTER DELTA}"  # Using the character name
'\u0394'
>>> "\u0394"                          # Using a 16-bit hex value
'\u0394'
>>> "\U00000394"                      # Using a 32-bit hex value
'\u0394'

```

Beyond that, a string can be built via the [`decode()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.decode) method belonging to [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes). The method accepts an *encoding* argument, like `UTF-8`, and optionally an *errors* argument.

The *errors* argument dictates how to react when the input string can’t be converted under the encoding’s rules. Permitted values here are `'strict'` (raise a [`UnicodeDecodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeDecodeError) exception), `'replace'` (use `U+FFFD`, `REPLACEMENT CHARACTER`), `'ignore'` (simply omit the character from the Unicode result), or `'backslashreplace'` (inserts a `\xNN` escape sequence). The examples below illustrate the distinctions:

```python
>>> b'\x80abc'.decode("utf-8", "strict")
Traceback (most recent call last):
    ...
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x80 in position 0:
  invalid start byte
>>> b'\x80abc'.decode("utf-8", "replace")
'\ufffdabc'
>>> b'\x80abc'.decode("utf-8", "backslashreplace")
'\\x80abc'
>>> b'\x80abc'.decode("utf-8", "ignore")
'abc'

```

You give encodings as strings holding the encoding’s name. Python ships with roughly 100 distinct encodings; the Python Library Reference lists them at [Standard Encodings](https://docs.python.org/3.14/library/codecs.html#standard-encodings). Certain encodings answer to several names; for instance, `'latin-1'`, `'iso_8859_1'` and `'8859`’ all refer to the same encoding.

The [`chr()`](https://docs.python.org/3.14/library/functions.html#chr) built-in function likewise produces one-character Unicode strings; it accepts integers and hands back a Unicode string of length 1 carrying the matching code point. The inverse is the built-in [`ord()`](https://docs.python.org/3.14/library/functions.html#ord) function, which accepts a one-character Unicode string and yields the code point value:

```python
>>> chr(57344)
'\ue000'
>>> ord('\ue000')
57344

```

[Subject index](INDEX.md) · [Previous source context](python-s-unicode-support.md) · [Following source context](converting-to-bytes.md)
