# Python 3.14.0 alpha 1 / core and builtins / files and paths

[gh-120754](https://github.com/python/cpython/issues/120754): Cut the count of system calls made while reading an entire file (for example `open('a.txt').read()`). Running a sample program that reads the 400+ `.rst` files under the cpython repository `Doc` folder shows the system call count falling by more than 10%.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
