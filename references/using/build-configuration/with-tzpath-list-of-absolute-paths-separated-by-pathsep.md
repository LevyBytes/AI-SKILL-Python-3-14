# --with-tzpath=&lt;list of absolute paths separated by pathsep&gt;

--with-tzpath=&lt;list of absolute paths separated by pathsep&gt;

Choose the default time zone search path used for [`zoneinfo.TZPATH`](https://docs.python.org/3.14/library/zoneinfo.html#zoneinfo.TZPATH). Refer to the [Compile-time configuration](https://docs.python.org/3.14/library/zoneinfo.html#zoneinfo-data-compile-time-config) belonging to the [`zoneinfo`](https://docs.python.org/3.14/library/zoneinfo.html#module-zoneinfo) module.

Default: `/usr/share/zoneinfo:/usr/lib/zoneinfo:/usr/share/lib/zoneinfo:/etc/zoneinfo`.

Refer to the [`os.pathsep`](https://docs.python.org/3.14/library/os.html#os.pathsep) path separator.

Added in version 3.9.

[Subject index](INDEX.md) · [Previous source section](with-suffix-suffix.md) · [Following source section](without-decimal-contextvar.md)
