# What’s New in Python 2.6 / PEP 3101: Advanced String Formatting

### PEP 3101: Advanced String Formatting

Within Python 3.0, the `%` operator gains a companion in the shape of a stronger string formatting approach, [`format()`](https://docs.python.org/3.14/library/functions.html#format). The [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) method's support has likewise been ported back into Python 2.6.

Under 2.6, every 8-bit string and Unicode string alike carries a `.format()` method that reads the string as a template and consumes the values you wish to format. That formatting template marks curly brackets (`{`, `}`) as its special characters:

```python
>>> # Substitute positional argument 0 into the string.
>>> "User ID: {0}".format("root")
'User ID: root'
>>> # Use the named keyword arguments
>>> "User ID: {uid}   Last seen: {last_login}".format(
...    uid="root",
...    last_login = "5 Mar 2008 07:20")
'User ID: root   Last seen: 5 Mar 2008 07:20'

```

To insert a literal curly bracket, double it up:

```python
>>> "Empty dict: {{}}".format()
"Empty dict: {}"

```

A field name may be an integer that points at a positional argument, like `{0}`, `{1}`, and so forth, or it may be a keyword argument's name. Compound field names are also permitted, letting you reach into attributes or pull values from dictionary keys:

```python
>>> import sys
>>> print 'Platform: {0.platform}\nPython version: {0.version}'.format(sys)
Platform: darwin
Python version: 2.6a1+ (trunk:61261M, Mar  5 2008, 20:29:41)
[GCC 4.0.1 (Apple Computer, Inc. build 5367)]'

>>> import mimetypes
>>> 'Content-type: {0[.mp4]}'.format(mimetypes.types_map)
'Content-type: video/mp4'

```

Keep in mind that with dictionary-style access like `[.mp4]`, surrounding the string with quotation marks is unnecessary; the lookup simply uses `.mp4` as its key. Any string that opens with a digit gets turned into an integer. More elaborate expressions cannot be embedded within a format string.

Up to this point we have only covered choosing which field goes into the final string. You can also govern the exact formatting by appending a colon and then a format specifier. As an illustration:

```python
>>> # Field 0: left justify, pad to 15 characters
>>> # Field 1: right justify, pad to 6 characters
>>> fmt = '{0:15} ${1:>6}'
>>> fmt.format('Registration', 35)
'Registration    $    35'
>>> fmt.format('Tutorial', 50)
'Tutorial        $    50'
>>> fmt.format('Banquet', 125)
'Banquet         $   125'

```

By nesting, a format specifier is allowed to point at other fields:

```python
>>> fmt = '{0:{1}}'
>>> width = 15
>>> fmt.format('Invoice #1234', width)
'Invoice #1234  '
>>> width = 35
>>> fmt.format('Invoice #1234', width)
'Invoice #1234                      '

```

You can also state how a field lines up inside the requested width:

| Character | Effect |
| --- | --- |
| < (default) | Left-align |
| > | Right-align |
| ^ | Center |
| = | (For numeric types only) Pad after the sign. |

A format specifier may further carry a presentation type that dictates the way the value is rendered. Floating-point numbers, for instance, can come out as an ordinary number or in exponential form:

[Subject index](INDEX.md) · [Previous source section](pep-371-the-multiprocessing-package-factorial.md) · [Next source section](pep-3101-advanced-string-formatting-d-to.md) · [Release/subject declaration](python-3-0.md)
