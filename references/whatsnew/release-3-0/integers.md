# What's New In Python 3.0 / Integers - sys

### Integers

- [**PEP 237**](https://peps.python.org/pep-0237/): In short, `long` got renamed to [`int`](https://docs.python.org/3.14/library/functions.html#int). Which is to say a single built-in integral kind exists now, called `int`; yet it acts for the most part like the former `long` kind.

- [**PEP 238**](https://peps.python.org/pep-0238/): A form such as `1/2` yields a float. To obtain truncation, reach for `1//2`. (That second spelling has been around for ages, going back at least to Python 2.2.)

- The `sys.maxint` constant is gone, because integer values now face no ceiling. That said, [`sys.maxsize`](https://docs.python.org/3.14/library/sys.html#sys.maxsize) works as an integer that exceeds any realistic list or string index. It tracks the implementation's ?natural? integer width and generally lines up with `sys.maxint` from earlier releases on the same platform (given identical build options).

- A long integer's [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) no longer carries the trailing `L`, so any code that strips that character without checking will lop off the final digit by mistake. (Reach for [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) in its place.)

- The `0720` form is no longer how octal literals are written; write `0o720` instead.

[Subject index](INDEX.md) · [Previous source section](ordering-comparisons.md) · [Next source section](text-vs-data-instead-of-unicode-vs-8-bit.md) · [Release/subject declaration](common-stumbling-blocks.md)
