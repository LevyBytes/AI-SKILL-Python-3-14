# Python 2.7 changes: Numeric precision and format-field changes

```python
>>> n = 295147905179352891391
>>> float(n)
2.9514790517935289e+20
>>> n - long(float(n))
-1L

```

(This was done by Mark Dickinson; [bpo-3166](https://bugs.python.org/issue?@action=redirect&bpo=3166).)

Rounding during integer division is more precise as well. (Mark Dickinson did this one too; [bpo-1811](https://bugs.python.org/issue?@action=redirect&bpo=1811).)

- Automatic coercion for complex numbers is gone; the interpreter will never again reach for a `__coerce__()` method on a complex object. (Taken out by Meador Inge and Mark Dickinson; [bpo-5211](https://bugs.python.org/issue?@action=redirect&bpo=5211).)

- Replacement fields can now be numbered automatically by the [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format) method. That brings `str.format()` usage nearer in feel to `%s` formatting:

```python
>>> '{}:{}:{}'.format(2009, 04, 'Sunday')
'2009:4:Sunday'
>>> '{}:{}:{day}'.format(2009, 4, day='Sunday')
'2009:4:Sunday'

```

Automatic numbering walks the fields in order from left to right, so the leading `{...}` specifier draws on the first argument passed to [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format), the following specifier on the following argument, and onward in that fashion. Auto-numbering can't be combined with explicit numbering — either give every specifier field a number or give none of them one — yet auto-numbering does coexist with named fields, exactly as the second snippet above shows. (Provided by Eric Smith; [bpo-5237](https://bugs.python.org/issue?@action=redirect&bpo=5237).)

Complex numbers now work properly with [`format()`](https://docs.python.org/3.14/library/functions.html#format) and fall back to right alignment. A precision or comma-separation setting reaches both the real and the imaginary halves of the value, whereas any chosen field width and alignment governs the entire `1.5+3j` rendering. (Provided by Eric Smith; [bpo-1588](https://bugs.python.org/issue?@action=redirect&bpo=1588) and [bpo-7988](https://bugs.python.org/issue?@action=redirect&bpo=7988).)

The "F" format code is now guaranteed to emit uppercase output, so you will see "INF" and "NAN" from it. (Provided by Eric Smith; [bpo-3382](https://bugs.python.org/issue?@action=redirect&bpo=3382).)

A subtler change: passing a format string to the [`object.__format__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__format__) method now raises a [`PendingDeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#PendingDeprecationWarning), since the `__format__()` implementation on [`object`](https://docs.python.org/3.14/library/functions.html#object) just renders the object as a string and formats that string. Formerly the method quietly handed the format string to the string representation, which had the potential to mask bugs in user code. After all, when you give an alignment or precision you presumably want the formatting carried out in some way tailored to the object. (Corrected by Eric Smith; [bpo-7994](https://bugs.python.org/issue?@action=redirect&bpo=7994).)

- A `bit_length` method was added to the [`int()`](https://docs.python.org/3.14/library/functions.html#int) and `long()` types; it reports how many bits are needed to write its argument in binary:

```python
>>> n = 37
>>> bin(n)
'0b100101'
>>> n.bit_length()
6
>>> n = 2**123-1
>>> n.bit_length()
123
>>> (n+1).bit_length()
124

```

(Provided by Fredrik Johansson and Victor Stinner; [bpo-3439](https://bugs.python.org/issue?@action=redirect&bpo=3439).)

- After a relative import such as `from .os import sep` fails, the [`import`](https://docs.python.org/3.14/reference/simple_stmts.html#import) statement will no longer fall back on attempting an absolute import. That corrects a defect, though it may also trip up the odd `import` statement that had only been functioning by chance. (Corrected by Meador Inge; [bpo-7902](https://bugs.python.org/issue?@action=redirect&bpo=7902).)

- A subclass of the built-in `unicode` type may now supply its own `__unicode__()` method to override the inherited one. (Done by Victor Stinner; [bpo-1583863](https://bugs.python.org/issue?@action=redirect&bpo=1583863).)

- `None` is now accepted as the first argument to the [`translate()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.translate) method on the [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) type. (Corrected by Georg Brandl; [bpo-4759](https://bugs.python.org/issue?@action=redirect&bpo=4759).)

- Wrapping a method with [`@classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod) or [`@staticmethod`](https://docs.python.org/3.14/library/functions.html#staticmethod) to make it a class or static method now leaves the original function reachable on the wrapper through its [`__func__`](https://docs.python.org/3.14/reference/datamodel.html#method.__func__) attribute. The author was Amaury Forgeot d — Arc, acting on an idea raised by George Sakkis; see [bpo-5982](https://bugs.python.org/issue?@action=redirect&bpo=5982).

- With a limited attribute set declared via `__slots__`, removing an attribute that was never assigned used to skip the [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) you would naturally anticipate. Corrected by Benjamin Peterson; [bpo-7604](https://bugs.python.org/issue?@action=redirect&bpo=7604).)

- Two extra encodings have joined the set: "cp720", mostly for Arabic text, and "cp858", which is CP 850 with the euro symbol tacked on. The cp720 codec came from Alexander Belchenko together with Amaury Forgeot d — Arc under [bpo-1616979](https://bugs.python.org/issue?@action=redirect&bpo=1616979), while Tim Hatch supplied cp858 under [bpo-8016](https://bugs.python.org/issue?@action=redirect&bpo=8016).

-

[Subject index](INDEX.md) · [Previous source section](core-language-changes.md) · [Next source section](file-errors-and-language-behavior.md) · [Release/subject declaration](the-future-for-python-2-x.md) · [Release/subject declaration](core-language-changes.md)
