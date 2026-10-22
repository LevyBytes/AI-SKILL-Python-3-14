# 7.1.3. Manual String Formatting

### 7.1.3. Manual String Formatting

Below is that very table of squares and cubes, this time laid out by hand:

```python
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # Note use of 'end' on previous line
...     print(repr(x*x*x).rjust(4))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000

```

(Bear in mind the single space separating each column comes from how [`print()`](https://docs.python.org/3.14/library/functions.html#print) behaves: it invariably inserts spaces between the arguments you give it.)

String objects carry a [`str.rjust()`](https://docs.python.org/3.14/library/stdtypes.html#str.rjust) method that right-justifies a string within a field of some width, filling the left side with spaces. Companion methods [`str.ljust()`](https://docs.python.org/3.14/library/stdtypes.html#str.ljust) and [`str.center()`](https://docs.python.org/3.14/library/stdtypes.html#str.center) exist as well. None of them write anything out; each merely hands back a fresh string. Where the supplied string runs too long, they leave it whole rather than clipping it; that throws off your column layout, but it generally beats the alternative of misstating a value. (Should clipping truly be what you want, you can always tack on a slice operation, like `x.ljust(n)[:n]`.)

One further method, [`str.zfill()`](https://docs.python.org/3.14/library/stdtypes.html#str.zfill), fills out the left of a numeric string with zeros. It is aware of plus and minus signs:

```python
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'

```

[Subject index](INDEX.md) · [Previous source section](the-string-format-method.md) · [Following source section](old-string-formatting.md)
