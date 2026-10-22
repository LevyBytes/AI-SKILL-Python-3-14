# sys._xoptions

sys._xoptions

A dictionary of the assorted implementation-specific flags handed in via the [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command-line option. Each option name maps either to the value spelled out for it, or else to [`True`](https://docs.python.org/3.14/library/constants.html#True). For instance:

```shell
$ ./python -Xa=b -Xc
Python 3.2a3+ (py3k, Oct 16 2010, 20:14:50)
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys._xoptions
{'a': 'b', 'c': True}

```

**CPython implementation detail:** This is CPython’s own route for reaching options handed in through [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X). Other implementations might surface them by different means, or leave them out entirely.

Added in version 3.2.

Citations

   [C99]

ISO/IEC 9899:1999. “Programming languages – C.” You can find a publicly posted draft of the standard over at [https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf).

[API family](INDEX.md) · [sys context index](../INDEX.md).
