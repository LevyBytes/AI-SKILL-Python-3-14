# Python 3.7.0 beta 1 / library / files and paths

[bpo-31961](https://bugs.python.org/issue?@action=redirect&bpo=31961): *Removed in Python 3.7.0b2.* A [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) is now permitted as the *args* argument to subprocess.Popen. Should *args* arrive as a sequence, a path-like object may now serve as its first element too.

[bpo-28134](https://bugs.python.org/issue?@action=redirect&bpo=28134): By default, sockets now derive family, type and protocol automatically from the file descriptor.

[bpo-32228](https://bugs.python.org/issue?@action=redirect&bpo=32228): Make `truncate()` keep the file position — the value `tell()` reports — intact following writes that exceed the buffer size.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
