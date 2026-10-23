# What’s New in Python 2.2 / Unicode Changes - zlib

### Unicode Changes

Release 2.2 brings a modest boost to Python’s Unicode handling. Typically Unicode strings live as UCS-2, stored as 16-bit unsigned integers. You can also build Python 2.2 so its internal encoding uses UCS-4, 32-bit unsigned integers, by handing `--enable-unicode=ucs4` to the configure script. (Passing `--disable-unicode` is likewise an option, switching Unicode support off altogether.)

A build using UCS-4 (a “wide Python”) lets the interpreter handle Unicode characters spanning U+000000 through U+110000 natively, which widens the band of permitted values for the `unichr()` function to match. On an interpreter built around UCS-2 (a “narrow Python”), any value above 65535 will still make `unichr()` throw a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) exception. The whole story appears in [**PEP 261**](https://peps.python.org/pep-0261/), “Support for ‘wide’ Unicode characters”; turn to it for the finer points.

The next change takes less explaining. From the start, Unicode strings have carried an `encode()` method that converts the string into a chosen encoding such as UTF-8 or Latin-1. Release 2.2 brings a matching `decode([*encoding*])` method to 8-bit strings (yet not to Unicode strings). `decode()` takes the string to be in the named encoding, decodes it accordingly, and returns whatever the codec produces.

This fresh capability has prompted the addition of codecs aimed at jobs that have nothing directly to do with Unicode. As examples, codecs now cover uu-encoding, MIME’s base64 encoding, and compression by way of the [`zlib`](https://docs.python.org/3.14/library/zlib.html#module-zlib) module:

```python
>>> s = """Here is a lengthy piece of redundant, overly verbose,
... and repetitive text.
... """
>>> data = s.encode('zlib')
>>> data
'x\x9c\r\xc9\xc1\r\x80 \x10\x04\xc0?Ul...'
>>> data.decode('zlib')
'Here is a lengthy piece of redundant, overly verbose,\nand repetitive text.\n'
>>> print s.encode('uu')
begin 666 <data>
M2&5R92!I<R!A(&QE;F=T:'D@<&EE8V4@;V8@<F5D=6YD86YT+"!O=F5R;'D@
>=F5R8F]S92P*86YD(')E<&5T:71I=F4@=&5X="X*

end
>>> "sheesh".encode('rot-13')
'furrfu'

```

To turn a class instance into Unicode, a class can supply a `__unicode__()` method, paralleling `__str__()`.

The `encode()`, `decode()`, and `__unicode__()` work was carried out by Marc-André Lemburg. Adapting the internals to operate on UCS-4 was the job of Fredrik Lundh and Martin von Löwis.

See also

[**PEP 261**](https://peps.python.org/pep-0261/) - Support for ‘wide’ Unicode characters

Authored by Paul Prescod.

[Subject index](INDEX.md) · [Previous source section](pep-238-changing-the-division-operator.md) · [Next source section](pep-227-nested-scopes.md) · [Release/subject declaration](introduction.md)
