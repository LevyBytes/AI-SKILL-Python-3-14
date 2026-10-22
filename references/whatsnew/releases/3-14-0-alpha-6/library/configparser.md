# Python 3.14.0 alpha 6 / library / configparser

[gh-129678](https://github.com/python/cpython/issues/129678): [`configparser.ConfigParser`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser): refrain from writing an empty unnamed section

[gh-128641](https://github.com/python/cpython/issues/128641): Brings back the performance of [`configparser.ConfigParser.read()`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser.read).

[gh-65697](https://github.com/python/cpython/issues/65697): The stdlib configparser will now try to confirm that the keys it writes won't corrupt the file (producing one that a later read() call from that same parser cannot parse accurately). A write() that would corrupt now raises an InvalidWriteError.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
