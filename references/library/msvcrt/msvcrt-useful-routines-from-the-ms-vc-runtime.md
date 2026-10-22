# msvcrt — `msvcrt` — Useful routines from the MS VC++ runtime

# Msvcrt

### `msvcrt` — Useful routines from the MS VC++ runtime

---

The routines here expose a handful of handy facilities specific to Windows. A few of the standard library's higher-level modules lean on them when wiring up their Windows-side behavior. As one illustration, the [`getpass`](https://docs.python.org/3.14/library/getpass.html#module-getpass) module relies on it internally to back its [`getpass()`](https://docs.python.org/3.14/library/getpass.html#module-getpass) function.

You can look up additional details about these routines in the Platform API documentation.

Both the ordinary and the wide-character flavors of the console I/O api are provided by this module. Because the ordinary API only understands ASCII characters, it is not much help once you need to support multiple languages; favor the wide-character API whenever you have the option.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

Changed in version 3.3: Calls in this module that used to signal [`IOError`](https://docs.python.org/3.14/library/exceptions.html#IOError) now report [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) instead.

[Subject index](INDEX.md) · [Continue](msvcrt-locking-to-msvcrt-get-osfhandle.md)
