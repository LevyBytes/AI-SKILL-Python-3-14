# How do I convert a string to a number?

### How do I convert a string to a number?

For whole numbers, reach for the built-in [`int()`](https://docs.python.org/3.14/library/functions.html#int) type constructor, as in `int('144') == 144`. In the same way, [`float()`](https://docs.python.org/3.14/library/functions.html#float) produces a floating-point number, as in `float('144') == 144.0`.

These default to reading the number as decimal, so `int('0144') == 144` is true, while `int('0x144')` raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). `int(string, base)` accepts the base to convert from as an optional second argument, hence `int( '0x144', 16) == 324`. When the base is given as 0, the number follows Python’s own rules: a leading ‘0o’ means octal, and ‘0x’ means a hex number.

Don't reach for the built-in [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) function when converting strings to numbers is your only aim. `eval()` runs much more slowly and brings a security hazard: a person could hand you a Python expression carrying unwanted side effects. As one example, somebody might pass `__import__('os').system("rm -rf $HOME")`, which would wipe out your home directory.

[`eval()`](https://docs.python.org/3.14/library/functions.html#eval) additionally treats numbers as Python expressions, which means, for instance, that `eval('09')` raises a syntax error, because Python forbids a leading ‘0’ in a decimal number (apart from ‘0’ itself).

[Subject index](INDEX.md)
