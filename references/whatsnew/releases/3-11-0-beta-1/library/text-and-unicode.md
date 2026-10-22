# Python 3.11.0 beta 1 / library / text and unicode

[gh-91984](https://github.com/python/cpython/issues/91984): Adjust test strings within test_argparse.py so they no longer carry trailing spaces ahead of the line ending.

[gh-91595](https://github.com/python/cpython/issues/91595): Corrects how a character is compared against an integer within `Tools.gdb.libpython.write_repr()`. Yu Liu supplied the patch.

[bpo-45995](https://bugs.python.org/issue?@action=redirect&bpo=45995): Introduce a “z” flag in the string formatting specification, which forces negative-zero floating-point values into positive zero once they have been rounded to the format precision. John Belmonte contributed this.

[bpo-44587](https://bugs.python.org/issue?@action=redirect&bpo=44587): Keep BooleanOptionalAction from appending a default string on its own. Should you want one, reach for a formatter to supply it.

[bpo-39716](https://bugs.python.org/issue?@action=redirect&bpo=39716): Throw an `ArgumentError` should a subparser name be registered a second time on an `argparse.ArgumentParser`. That matches the (default) behavior already seen when an option string is registered twice on an `ArgumentParser`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
