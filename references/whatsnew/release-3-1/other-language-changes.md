# What’s New In Python 3.1 / Other Language Changes - string

### Other Language Changes

A handful of more modest tweaks landed in the core Python language:

- Folders and zip archives that hold a `__main__.py` file may now run straight away once their name is handed to the interpreter. That directory or zipfile is placed automatically as sys.path's leading entry. (Andy Chu supplied the idea and a first patch; Phillip J. Eby and Nick Coghlan reworked that patch; [bpo-1739468](https://bugs.python.org/issue?@action=redirect&bpo=1739468).)

- A `bit_length` method was added to the [`int()`](https://docs.python.org/3.14/library/functions.html#int) type; it reports how many bits are needed to express its argument in binary form:

```python
>>> n = 37
>>> bin(37)
'0b100101'
>>> n.bit_length()
6
>>> n = 2**123-1
>>> n.bit_length()
123
>>> (n+1).bit_length()
124

```

(Contributed by Fredrik Johansson, Victor Stinner, Raymond Hettinger, and Mark Dickinson; [bpo-3439](https://bugs.python.org/issue?@action=redirect&bpo=3439).)

- Within [`format()`](https://docs.python.org/3.14/library/functions.html#format) strings, the fields may now receive numbers on their own:

```python
>>> 'Sir {} of {}'.format('Gallahad', 'Camelot')
'Sir Gallahad of Camelot'

```

Earlier on, you would have had to spell out numbered fields like: `'Sir {0} of {1}'`.

(Contributed by Eric Smith; [bpo-5237](https://bugs.python.org/issue?@action=redirect&bpo=5237).)

- With `string.maketrans()` now deprecated, two fresh static methods take over: [`bytes.maketrans()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.maketrans) and [`bytearray.maketrans()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.maketrans). The move clears up the muddle over which types the [`string`](https://docs.python.org/3.14/library/string.html#module-string) module actually handled. These days, [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) come with their own **maketrans** and **translate** methods, using intermediate translation tables matched to each type.

(Contributed by Georg Brandl; [bpo-5675](https://bugs.python.org/issue?@action=redirect&bpo=5675).)

- The grammar of the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement now lets you list several context managers within one statement:

```python
>>> with open('mylog.txt') as infile, open('a.out', 'w') as outfile:
...     for line in infile:
...         if '<critical>' in line:
...             outfile.write(line)

```

Thanks to this grammar, the `contextlib.nested()` function has become unnecessary and is now deprecated.

(Contributed by Georg Brandl and Mattias Brändström; [appspot issue 53094](https://codereview.appspot.com/53094).)

- When *x* is an integer, `round(x, n)` now hands back an integer rather than the float it used to give:

```python
>>> round(1123, -2)
1100

```

(Contributed by Mark Dickinson; [bpo-4707](https://bugs.python.org/issue?@action=redirect&bpo=4707).)

- To find the briefest floating-point spelling that keeps a value intact, Python now applies David Gay’s algorithm. The goal is to ease some of the puzzlement that surrounds binary floating-point numbers.

You can see why this matters with a value such as `1.1`, which lacks any precise counterpart in binary floating point. With no exact match available, an expression like `float('1.1')` resolves to the closest representable value, namely `0x1.199999999999ap+0` in hex or `1.100000000000000088817841970012523233890533447265625` written out in decimal. That closest value was, and remains, what later floating-point arithmetic relies on.

The change concerns the way the number appears on screen. Earlier, Python took a basic route. It worked out `repr(1.1)` as `format(1.1, '.17g')`, which came out to `'1.1000000000000001'`. Going with 17 digits had the benefit of leaning on IEEE-754 guarantees so that `eval(repr(1.1))` would round-trip back exactly to where it started. The drawback was that plenty of people found that result baffling (taking the inherent limits of binary floating-point representation for a flaw in Python on its own).

For `repr(1.1)`, the fresh algorithm is cleverer and yields `'1.1'`. In effect, it scans every equivalent string spelling (those saved against the identical underlying float value) and gives back the shortest one.

While the fresh algorithm leans toward tidier output where it can, the values underneath stay the same. Hence it remains true that `1.1 + 2.2 != 3.3`, regardless of what the spellings might imply.

This fresh algorithm counts on particular capabilities in the floating-point implementation underneath. Should those needed capabilities be absent, the prior algorithm stays in service. On top of that, the text pickle protocols keep cross-platform portability intact by sticking with the prior algorithm.

(Contributed by Eric Smith and Mark Dickinson; [bpo-1580](https://bugs.python.org/issue?@action=redirect&bpo=1580))

[Subject index](INDEX.md) · [Previous source section](pep-378-format-specifier-for-thousands-separator.md) · [Release/subject declaration](pep-372-ordered-dictionaries.md) · [Next source section](standard-library-module-changes.md)
