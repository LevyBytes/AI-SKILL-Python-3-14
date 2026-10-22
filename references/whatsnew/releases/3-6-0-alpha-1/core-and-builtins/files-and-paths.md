# Python 3.6.0 alpha 1 / core and builtins / files and paths

[bpo-26289](https://bugs.python.org/issue?@action=redirect&bpo=26289): Tune the floor and modulo division paths for longs of a single digit. Across microbenchmarks the gain lands at 2-2.5x. The built-in "divmod" function picks up roughly 10% of speed on top of that. (See also: [bpo-26315](https://bugs.python.org/issue?@action=redirect&bpo=26315))

[bpo-20120](https://bugs.python.org/issue?@action=redirect&bpo=20120): Parse .pypirc with RawConfigParser, dropping the interpolation support that had crept in unintentionally during the Python 3 move. .pypirc files now skip interpolation entirely, lining up with how Python 2.7 and Setuptools 19.0 behaved.

[bpo-26581](https://bugs.python.org/issue?@action=redirect&bpo=26581): Where a coding cookie appears more than once on a single line of a Python source file, only its first occurrence is honored.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
