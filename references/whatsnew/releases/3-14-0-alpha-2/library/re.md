# Python 3.14.0 alpha 2 / library / re

[gh-67877](https://github.com/python/cpython/issues/67877): Plug the memory leaks that occurred when [`regular expression`](https://docs.python.org/3.14/library/re.html#module-re) matching halted suddenly, whether from a signal or from a failed memory allocation.

[gh-126505](https://github.com/python/cpython/issues/126505): Repair two bugs when compiling case-insensitive [`regular expressions`](https://docs.python.org/3.14/library/re.html#module-re) whose character classes hold non-BMP characters: an upper-case non-BMP character was being skipped, and the ASCII flag was disregarded while matching a character range with an upper bound past the BMP region.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
