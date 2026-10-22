# What's New In Python 3.11 / math — math

### math

- [`math.exp2()`](https://docs.python.org/3.14/library/math.html#math.exp2) was added: it gives 2 raised to the power of x. (Contributed by Gideon Mitchell in [bpo-45917](https://bugs.python.org/issue?@action=redirect&bpo=45917).)

- [`math.cbrt()`](https://docs.python.org/3.14/library/math.html#math.cbrt) was added: it gives the cube root of x. (Contributed by Ajith Ramachandran in [bpo-44357](https://bugs.python.org/issue?@action=redirect&bpo=44357).)

- Two boundary cases of [`math.pow()`](https://docs.python.org/3.14/library/math.html#math.pow) had their behaviour adjusted to align with the IEEE 754 specification. Both `math.pow(0.0, -math.inf)` and `math.pow(-0.0, -math.inf)` now yield `inf`. Formerly each one raised [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). (Contributed by Mark Dickinson in [bpo-44339](https://bugs.python.org/issue?@action=redirect&bpo=44339).)

- The [`math.nan`](https://docs.python.org/3.14/library/math.html#math.nan) value can now be reached at all times. (Contributed by Victor Stinner in [bpo-46917](https://bugs.python.org/issue?@action=redirect&bpo=46917).)

[Subject index](INDEX.md) · [Previous source section](logging.md) · [Next source section](operator.md) · [Release/subject declaration](summary-release-highlights.md)
