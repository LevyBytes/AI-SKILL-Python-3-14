# What's New In Python 3.11 / fractions — fractions

### fractions

- [**PEP 515**](https://peps.python.org/pep-0515/)-style construction of a [`Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction) from a string is now supported. (Contributed by Sergey B Kirpichev in [bpo-44258](https://bugs.python.org/issue?@action=redirect&bpo=44258).)

- [`Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction) now carries an `__int__` method, which lets an `isinstance(some_fraction, typing.SupportsInt)` test succeed. (Contributed by Mark Dickinson in [bpo-44547](https://bugs.python.org/issue?@action=redirect&bpo=44547).)

[Subject index](INDEX.md) · [Previous source section](fcntl.md) · [Next source section](functools.md) · [Release/subject declaration](summary-release-highlights.md)
