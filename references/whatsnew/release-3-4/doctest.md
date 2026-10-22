# What's New In Python 3.4 / doctest — argparse, doctest, unittest

### doctest

A new [option flag](https://docs.python.org/3.14/library/doctest.html#doctest-options), [`FAIL_FAST`](https://docs.python.org/3.14/library/doctest.html#doctest.FAIL_FAST), stops the test run the instant the first failure shows up. (Contributed by R. David Murray and Daniel Urban in [bpo-16522](https://bugs.python.org/issue?@action=redirect&bpo=16522).)

The [`doctest`](https://docs.python.org/3.14/library/doctest.html#module-doctest) command line interface relies on [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) now and gains two new options, `-o` and `-f`. `-o` lets [doctest options](https://docs.python.org/3.14/library/doctest.html#doctest-options) be given on the command line, while `-f` abbreviates `-o FAIL_FAST` (mirroring the comparable option that the [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) CLI provides). (Contributed by R. David Murray in [bpo-11390](https://bugs.python.org/issue?@action=redirect&bpo=11390).)

[`doctest`](https://docs.python.org/3.14/library/doctest.html#module-doctest) will from now on locate doctests within the `__doc__` strings of extension modules. (Contributed by Zachary Ware in [bpo-3158](https://bugs.python.org/issue?@action=redirect&bpo=3158).)

[Subject index](INDEX.md) · [Previous source section](dis.md) · [Next source section](email.md) · [Release/subject declaration](release-highlights.md)
